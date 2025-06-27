from fastapi import APIRouter
from controllers.ItemController import add_Item, find_all_Items
from models.Items import Item

router = APIRouter()

@router.post('/add_item')
async def create_item(item: Item):
    return await add_Item(item)


@router.get('/all_imtes')
async def all_items():
    return await find_all_Items()