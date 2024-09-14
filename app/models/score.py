from pydantic import BaseModel
from typing import Union

class Score(BaseModel):
    id: int
    name: str