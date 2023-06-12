import torch
print(torch.cuda.is_available())
from pathlib import Path
import json
from llama import ModelArgs, Transformer, Tokenizer, LLaMA

from fairscale.nn.model_parallel.initialize import initialize_model_parallel
import os
from typing import Tuple
import time

def setup_model_parallel() -> Tuple[int, int]:
    local_rank = int(os.environ.get("LOCAL_RANK", -1))
    world_size = int(os.environ.get("WORLD_SIZE", -1))

    torch.distributed.init_process_group("nccl")
    initialize_model_parallel(world_size)
    torch.cuda.set_device(local_rank)

    # seed must be the same in all processes
    torch.manual_seed(1)
    return local_rank, world_size

start_time = time.time()
torch.distributed.init_process_group("nccl")
world_size = int(os.environ.get("WORLD_SIZE", -1))
initialize_model_parallel(world_size)
torch.manual_seed(1)
local_rank = 1

ckpt_dir = '/scratch/raghav.arora/llama/13b/'
checkpoints = sorted(Path(ckpt_dir).glob("*.pth"))

ckpt_path = checkpoints[local_rank]
torch.cuda.empty_cache()
device = 'cpu'
checkpoint = torch.load(ckpt_path, map_location=device)
checkpoint = {k: v.to(device) for k, v in checkpoint.items()}
with open(Path(ckpt_dir) / "params.json", "r") as f:
    params = json.loads(f.read())

model_args: ModelArgs = ModelArgs(
    max_seq_len=256, max_batch_size=16, **params
)
tokenizer_path = '/scratch/raghav.arora/llama/tokenizer.model'
tokenizer = Tokenizer(model_path=tokenizer_path)
model_args.vocab_size = tokenizer.n_words

torch.set_default_tensor_type(torch.FloatTensor)
model = Transformer(model_args).to(device)
model.load_state_dict(checkpoint, strict=False)
generator = LLaMA(model, tokenizer)
print(f"Loaded in {time.time() - start_time:.2f} seconds")
