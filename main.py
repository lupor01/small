from fastapi import FastAPI, Header, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import joblib
import numpy as np
 
# print(fastapi.__version__)

# classifier = pipeline("sentiment-analysis")
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# class TextInput(BaseModel): # make sure it matches!!!
#     text: str # INPUT VALIDATION

# API_KEY = "segretissimo"

# def verify_key(api_key: str = Header(...)):
#     if api_key != API_KEY:
#         raise HTTPException(status_code=401, detail="API key not valid")

# @app.post("/sentiment")
# def analyse(data: TextInput, api_key: str = Depends(verify_key)) -> dict:
#     result = classifier(data.text)[0] # predition here!!!
#     return {
#         "label": result["label"],
#         "score": float(result["score"])
#     }