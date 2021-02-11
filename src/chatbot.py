from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

step = 0


def read_chat(text):
    new_user_input_ids = tokenizer.encode(
        text + tokenizer.eos_token, return_tensors="pt"
    )
    bot_input_ids = (
        torch.cat([0, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
    )

    chat_history_ids = model.generate(
        bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
    )
    # step = step + 1
    # pretty print last ouput tokens from bot
    ans = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1] :][0], skip_special_tokens=True
    )
    return ans


@app.get("/chat")
def read_item(text: str):
    ans = read_chat(text)

    return {"Answer": ans}
