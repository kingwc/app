from fastapi import FastAPI, Depends
from module import crud
from app_database import Base, engine


app = FastAPI()

app.include_router(crud.router)

"""
Test GET endpoint.
"""

@app.get("/")
async def index():
    return {"message": "Hi Weslee 🤓"}

@app.on_event('startup')
def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tables created")