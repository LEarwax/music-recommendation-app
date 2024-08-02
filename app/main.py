from fastapi import FastAPI
from api.routes.comments import router as comments_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(comments_router, prefix="/api")