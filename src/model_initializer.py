import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def initialize_model(model_name="EleutherAI/gpt-j-6B"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
    model.to(device)
    return model, tokenizer
