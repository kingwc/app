import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from app_database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    epic_id = Column(String(128))
    email = Column(String(128))
    hashed_password = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    hours_played = Column(Integer, default=0)
    is_banned = Column(Boolean, default=False)
    games_played_count = Column(Integer, default=0)
    pfp_link = Column(String, default="assets/images/user/default_pfp.png")

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    type_id = Column(Integer) # 1 = solo, 2 = duo, 3 = trio, 4 = squads
    is_ranked = Column(Boolean)
    duration = Column(Integer) # measured in seconds