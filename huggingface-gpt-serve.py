import transformers
import torch

# Deploying huggingface transformers GPT2 with flask
# https://github.com/huggingface/transformers/blob/master/examples/run_gpt_serve.py


# Load GPT2 tokenizer
tokenizer = transformers.GPT2Tokenizer.from_pretrained("gpt2")


# Load GPT2 model
model = transformers.GPT2LMHeadModel.from_pretrained("gpt2")
model.to(torch.device("cpu"))
model.eval()


# Define flask app
from flask import Flask, request, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True


# Flask routes
@app.route("/")
def index():
    return "Index API"


@app.route("/api/v1/tokenize", methods=["POST"])
def tokenize():
    # Get text
    text = request.json["text"]

    # Tokenize text
    tokens = tokenizer.encode(text)

    # Return tokenized text
    return jsonify({"tokens": tokens})


@app.route("/api/v1/translate", methods=["POST"])
def translate():
    # Get text
    text = request.json["text"]

    # Tokenize text
    tokens = tokenizer.encode(text)

    # Translate text
    translated = model.generate(tokens)

    # Return translated text
    return jsonify({"translated": translated})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)