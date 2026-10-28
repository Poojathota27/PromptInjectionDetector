from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import DistilBertTokenizerFast
from transformers import DistilBertForSequenceClassification

app = FastAPI(
    title="Prompt Injection Detection API",
    version="1.0.0"
)

MODEL_PATH = "distilbert-prompt-injection"

labels = {
    0: "Benign",
    1: "Direct Injection",
    2: "Indirect Injection",
    3: "Jailbreak"
}

tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)

model = DistilBertForSequenceClassification.from_pretrained(
    MODEL_PATH
)

model.eval()


class PromptRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "Prompt Injection Detection API is running"
    }


@app.post("/predict")
def predict(request: PromptRequest):

    inputs = tokenizer(
        request.text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

        probabilities = torch.softmax(
            outputs.logits,
            dim=1
        )

        prediction = torch.argmax(
            probabilities,
            dim=1
        ).item()

        confidence = probabilities[
            0, prediction
        ].item()

    return {
        "prediction": labels[prediction],
        "label": prediction,
        "confidence": confidence
    }