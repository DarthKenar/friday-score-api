from fastapi import APIRouter
from app.models.car import Car
from typing import Union

car_router = APIRouter()
car_router.tags = ['Cars']

@car_router.get("/{car_id}")
def read_item(car_id: int, q: Union[str, None] = None):
    return {"car_id": car_id, "q": q}

@car_router.put("/{car_id}")
def update_item(car_id: int, car: Car):
    return {"car_name": car.name, "car_id": car_id}

@car_router.delete("/{car_id}")
def delete_item(car_id: int, car_name: Union[str, None] = None):
    return {"car_name": car_name, "car_id": car_id}