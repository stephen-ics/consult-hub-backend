from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from .database import engine
# from . import models
from app.routers import checkout


# from .config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

origins = ["*"]  # Disables cors for all domains --> security issue will change later

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(checkout.router)


@app.get("/")
def root():
    return {"message": "Hello World! 1333"}
