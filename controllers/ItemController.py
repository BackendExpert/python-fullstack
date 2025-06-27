from fastapi import HTTPException
from config.DB import db
from models.Items import Item

collection = db['Items']

async def add_Item(item: Item):
    result = await collection.insert_one(item.dict())
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="fail to add Items")
    return { "Message": "Item Added","id": str(result.inserted_id) }


async def find_all_Items():
    itemall = collection.find()
    items = []

    async for item in itemall:
        item['id'] = str(item["_id"])
        del item['_id']
        items.append(item)

    return items
