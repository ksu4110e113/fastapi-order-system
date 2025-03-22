from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class MenuItem(BaseModel):
    name: str
    price: int
    intro: str


@app.get("/")
def read_root():
    return [
    {"name": "炸雞", "price": 120, "intro": "酥脆多汁"},
    {"name": "珍奶", "price": 60, "intro": "香濃黑糖 Q 彈珍珠"}
    ]