from typing import Union
import torch
from fastapi import FastAPI, File, UploadFile
from classifier.classify import classify

app = FastAPI()

model = torch.load("classifier/model.pth")
model.eval()

print("Loaded model")

@app.post("/classify")
async def classify_pokemon(pokemon_img: UploadFile):
    data = await pokemon_img.read()
    return classify(data, model)
