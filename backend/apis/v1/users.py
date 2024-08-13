from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import UserCreate
from db.session import get_db
from db.models.users import Users
from db.repositories.users import createUser


router = APIRouter()

@router.post("/")
def recordUser(dto:UserCreate,
               db:Session= Depends(get_db())):
    return createUser(dto, db)