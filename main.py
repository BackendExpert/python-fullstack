from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_main():
    return {"message": "Backend is Working fine...."}
