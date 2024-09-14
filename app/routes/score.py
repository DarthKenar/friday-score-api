import json
from fastapi import APIRouter
from app.models.score import Score
from typing import Union

score_router = APIRouter()
score_router.tags = ['Score']

@score_router.get("/")
def read_scores():
    with open('./app/db/data.json', 'r') as file:
        data = json.load(file)
    return data
