from typing import Union, Optional	
from app.routes import score
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

app.include_router(score.score_router, prefix='/score', tags=['Score'])


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)