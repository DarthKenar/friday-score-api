from typing import Union, Optional	
from app.routes import score
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

app.include_router(item.item_router, prefix='/score', tags=['Score'])
