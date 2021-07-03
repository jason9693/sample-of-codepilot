import transformers
import torch

# Deploying huggingface transformers BERT with flask
# https://github.com/huggingface/transformers/blob/master/examples/run_bert_classifier.py


# Initialize PyTorch device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Initialize transformers model
bert_model = "bert-base-uncased"
bert_tokenizer = transformers.BertTokenizer.from_pretrained(bert_model)
bert_model = transformers.BertModel.from_pretrained(bert_model)
bert_model.to(device)


# Initialize flask app
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/", methods=["POST"])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    text = data["text"]
    # Tokenize input text
    tokenized_text = bert_tokenizer.tokenize(text)
    # Convert token to id
    indexed_tokens = bert_tokenizer.convert_tokens_to_ids(tokenized_text)
    # Convert id to token
    tokens_tensor = torch.tensor([indexed_tokens])
    # Predict
    with torch.no_grad():
        prediction = bert_model(tokens_tensor)
    # Convert prediction to list
    predictions = prediction.tolist()
    # Return list as response
    return jsonify(predictions[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    