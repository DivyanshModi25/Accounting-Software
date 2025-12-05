from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic 
    # await init_db

    yield

    # shutdown logic
    # await close_db()


app = FastAPI(
    title="Accounting software API",
    version="1.0.0",
    lifespan=lifespan,  # register lifespan handler 
)


# origins = [
#     "http://localhost:3000",  # e.g. React frontend
#     "http://127.0.0.1:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,          # or ["*"] during development
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# app.include_router(api_v1_router, prefix="/v1")


#  healthcheck
@app.get("/health")
async def health():
    return {"status": "ok"}

