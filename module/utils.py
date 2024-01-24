from sqlalchemy.orm import Session
from fastapi import HTTPException
from .models import User, Game
from .schemas import UserCreate, GameCreate

"""
Find user from database using epic_id as query parameter.
"""
def user_by_epic_id(epic_id: str, db: Session):
    db_user = db.query(User).filter(User.epic_id == epic_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


"""
Check database if epic_id is already in use
"""
def check_existing_epic_id(id: str, db: Session):
    db_user = db.query(User).filter(User.epic_id == id).first()
    if db_user is not None:
        raise HTTPException(status_code=409, detail="This epic ID is already in use")

"""
Check database if email is already in use
"""
def check_existing_email_id(id: str, db: Session):
    db_user = db.query(User).filter(User.email == id).first()
    if db_user is not None:
        raise HTTPException(status_code=409, detail="This email is already in use")


"""
Function to "hash" password.
"""
def hash_password(password: str):
    return password + "FAKEHASH312321"

"""
Create user using POST parameters from UserCreate schema
"""
def create_user(user: UserCreate, db: Session):
    db_user = User(
        epic_id=user.epic_id,
        email=user.email,
        hashed_password=hash_password(user.password),
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message:", "Successfully created account for user {}".format(db_user.epic_id)}


"""
GET game by game ID. 
"""
def game_by_id(id: int, db: Session):
    db_game = db.query(Game).filter(Game.id == id).first()
    if db_game is None:
        raise HTTPException(status_code=404, detail="This game does not exist")
    return db_game


"""
Create a record for a new game played. 
"""
def new_game_record(game: GameCreate, db: Session):
    db_game = Game(
        type_id=game.type_id,
        is_ranked=game.is_ranked,
        duration=game.duration,
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    return {"message", "Successfully created new game"}