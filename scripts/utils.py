import torch
import open_clip


def gen_clip_lang_embeddings(text, model_name):
    pretrained = {
        'ViT-H/14': 'laion2b_s32b_b79k',
        'convnext_base': 'laion400m_s13b_b51k',
        'RN50': 'openai'
    }
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = torch.load('vit_model.pth')
    model_name = model_name.replace('/', '-')
    tokenizer = open_clip.get_tokenizer(model_name)
    text = tokenizer([text]).to(device)
    with torch.no_grad(), torch.cuda.amp.autocast():
        text_features = model.encode_text(text)
        text_features /= text_features.norm(dim=-1, keepdim=True)
    return text_features
