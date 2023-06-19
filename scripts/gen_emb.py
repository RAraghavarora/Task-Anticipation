from utils import gen_clip_lang_embeddings
import numpy as np

with open('morning.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

clip_dict = {}
for line in lines:
    clip_emb = gen_clip_lang_embeddings(line, "ViT-H/14")
    clip_dict[line] = clip_emb.squeeze(0)

np.save('morning.npy', clip_dict)
