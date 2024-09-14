from pydantic import BaseModel
from typing import Union

class Step_one(BaseModel):
    id: int
    name: str