import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class GPT2Agent:
    def __init__(self, model_path, device="cuda"):
        self.model = GPT2LMHeadModel.from_pretrained(model_path).to(device)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
        self.device = device

    def generate_response(self, prompt, temperature=0.9):
        prompt = f"<USER>: {prompt} <BOT>:"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, padding=True).to(self.device)

        output = self.model.generate(
            inputs.input_ids,
            pad_token_id=self.tokenizer.eos_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            do_sample=True,
            temperature=temperature,
            attention_mask=inputs.attention_mask if "attention_mask" in inputs else None
        )

        decoded = self.tokenizer.decode(output[0], skip_special_tokens=True).strip()
        return decoded.split("\n")[0].split("<BOT>:")[1]

    def update_model(self, new_model_path):
        self.model = GPT2LMHeadModel.from_pretrained(new_model_path).to(self.device)
        self.tokenizer = GPT2Tokenizer.from_pretrained(new_model_path)