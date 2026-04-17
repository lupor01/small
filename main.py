import os
import sqlite3

from fastapi import FastAPI, Header, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from jinja2 import Environment, FileSystemLoader
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import transformers 


app = FastAPI()


# escape localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# handling JS, CSS and HTML
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# GET home
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# nlp stuff
classifier = transformers.pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
class TextInput(BaseModel): # make sure it matches!!!
    text: str # INPUT VALIDATION


# KEY: DON'T HARDCODE IN ACTUAL DEPLOYMENT!
API_KEY = os.getenv("API_KEY")

def verify_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API key not valid")
    return True
    

# model response
@app.post("/sentiment")
def analyse(data: TextInput, api_key: str = Depends(verify_key)) -> dict:
    result = classifier(data.text)[0] # predition here!!!
    label = result["label"]
    score = float(result["score"])

    with sqlite3.connect("small.db") as con:
        con.execute("INSERT INTO Sentiment (Feedback, Score) VALUES (?, ?)", (data.text, score))

    return {
        "label": label,
        "score": score
    }