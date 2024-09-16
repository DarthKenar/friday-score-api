import json
from fastapi import APIRouter
from app.models.score import Data
from app.models.request import Write_score_titles
from typing import Union

score_router = APIRouter()
score_router.tags = ['Score']

@score_router.get("/")
def read_scores():
    with open('./app/db/data.json', 'r') as file:
        data:Data = json.load(file)
    return data

@score_router.put("/titles")
def write_score_titles(titles:Write_score_titles):
    with open('./app/db/data.json', 'rw') as file:
        data:Data = json.load(file)
        for title in titles:
            data['steps'].find(title['key'])['title'] = title['title']
    return data