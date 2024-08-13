from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base

def createTables():
    Base.metadata.create_all(bind=engine)

def startApplication():
    app= FastAPI(title= settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    createTables()
    return app

app=startApplication()

@app.get("/")
def helloWorld():
    return {"detail":"Hellow World"}

