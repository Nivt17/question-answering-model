import question_answering_model as fl
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow_hub as hub
import json

class Item(BaseModel):
    questions: set
    paragraph: str
        
app = FastAPI()


@app.get("/")
async def root():
    return "This is a question answering model"

@app.post("/predict/")
def predict(item: Item):
    return fl.getAnswer(item.questions, item.paragraph, model)

model = hub.load('https://github.com/see--/natural-question-answering/releases/download/v0.0.1/model.tar.gz')
