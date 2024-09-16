from pydantic import BaseModel
from typing import List

class ItemStep(BaseModel):
    title: int
    score: str
class Step(BaseModel):
    key: str
    title: str
    items: List[ItemStep]
    weight: int

class Data(BaseModel):
    steps: List[Step]

