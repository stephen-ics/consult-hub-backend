from fastapi import FastAPI, Response, HTTPException, Depends, APIRouter

# from sqlalchemy.orm import Session
from typing import List, Optional

# from .. import models, schemas, oauth2
# from ..database import get_db
# from sqlalchemy import func, asc

router = APIRouter(prefix="/checkout", tags=["Post"])


@router.post("/create-checkout-session", response_model=List[schemas.PostResponse])
def create_checkout_session():
    return {"message": "success"}
