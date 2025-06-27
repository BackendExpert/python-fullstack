from fastapi import APIRouter
from controllers.ItemController import add_Item
from models.Items import Item

router = APIRouter()

router.post('/')

async def create_item(item: Item):
    return add_Item(item)