from sqlalchemy.orm import Session
from schemas.users import UserCreate
from db.models.users import Users

def createUser(dto:UserCreate, db: Session)-> Users:
    user=Users(
        username=dto.username,
        email=dto.email,
        password=dto.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user