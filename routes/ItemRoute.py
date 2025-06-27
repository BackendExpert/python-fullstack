from fastapi import APIRouter
from controllers.ItemController import add_Item
from models.Items import Item

router = APIRouter()

@router.post('/add_item')
async def create_item(item: Item):
    return await add_Item(item)