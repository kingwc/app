
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from .utils import check_existing_email_id, check_existing_epic_id, game_by_id, new_game_record, user_by_epic_id, create_user
from .schemas import UserCreate, UserGet, GameCreate, GameGet

from app_database import get_db

router = APIRouter()

"""
Create user using POST endpoint from UserCreate schema.
"""
@router.post("/user/create")
async def create_user_post(user: UserCreate, db: Session = Depends(get_db)):
    check_existing_epic_id(id=user.epic_id, db=db)
    check_existing_email_id(id=user.email, db=db)
    
    return create_user(user=user, db=db)

"""
GET requestion for user data based off of epic_id query parameter.
"""
@router.get("/user/{epic_id}", response_model=UserGet)
async def get_user_by_epic_id(epic_id: str, db: Session = Depends(get_db)):
    return user_by_epic_id(epic_id=epic_id, db=db)


"""
GET request for game data based off of game id query parameter. 
"""
@router.get("/games/{id}", response_model=GameGet)
async def get_game_by_id(id: int, db: Session = Depends(get_db)):
    return game_by_id(id=id, db=db)

@router.post("/games/new")
async def new_game(game: GameCreate, db: Session = Depends(get_db)):
    return new_game_record(game=game, db=db)