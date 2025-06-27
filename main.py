from fastapi import FastAPI
from routes.ItemRoute import router as ItemRouter

app = FastAPI()

app.include_router(ItemRouter, prefix='/items')

@app.get('/')
def read_main():
    return {"message": "Backend is Working fine...."}
