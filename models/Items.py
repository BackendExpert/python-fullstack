from pydantic import BaseModel

class Item (BaseModel):
    name: str
    desc: str
    price: float

