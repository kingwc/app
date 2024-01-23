from pydantic import BaseModel

class GameBase(BaseModel):
    pass

class GameGet(GameBase):
    id: int
    type_id: int
    is_ranked: bool
    duration: int

class GameCreate(GameBase):
    type_id: int
    is_ranked: bool
    duration: int

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    epic_id: str
    email: str
    password: str

class UserGet(UserBase):
    id: int
    epic_id: str
    email: str
    hours_played: int
    is_banned: bool
    games_played: int
    pfp_link: str

    class Config:
        orm_mode = True