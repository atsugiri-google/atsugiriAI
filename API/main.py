from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

model_name = "distilgpt2"  # 軽量モデル
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    text = data.get("message", "")

    inputs = tokenizer(text, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=50)
    reply = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
