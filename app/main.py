from fastapi import FastAPI,Depends
from app.api.routes import router



app = FastAPI()

app.include_router(router)

@app.get("/")
def health():
    return {"status":"healthy"}
