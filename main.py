import os
import sqlite3

from fastapi import FastAPI, Header, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import transformers 


app = FastAPI()

with sqlite3.connect("small.db") as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Sentiment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Feedback TEXT,
            Score REAL
        )
    """)


# escape localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
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
if API_KEY is None:
    raise RuntimeError("API_KEY not defined in environment")

def verify_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API key not valid")
    return True


# model response
@app.post("/sentiment")
def analyse(data: TextInput, api_key: str = Depends(verify_key)) -> dict:
    result = classifier(data.text)[0] # predition here!!!

    with sqlite3.connect("small.db") as con:
        con.execute(
            "INSERT INTO Sentiment (Feedback, Score) VALUES (?, ?);",
            (data.text, float(result["score"]))
        )

    return {
        "label": result["label"],
        "score": float(result["score"])
    }