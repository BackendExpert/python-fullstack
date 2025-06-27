from fastapi import FastAPI
from routes.ItemRoute import create_item

app = FastAPI()

@app.get('/')
def read_main():
    return {"message": "Backend is Working fine...."}
