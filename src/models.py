from flask_sqlalchemy import SQLAlchemy
from typing import List
from sqlalchemy import String, Boolean, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__="users"
    user_id:Mapped[int] = mapped_column(Integer,primary_key=True)
    nickname:Mapped[str]= mapped_column(String(50),unique=True,nullable=False)
    user_name:Mapped[str]= mapped_column(String(40),nullable=False)
    last_name:Mapped[str]=mapped_column(String(40),nullable=False)
    email:Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    account:Mapped["Account"]=relationship(
        back_populates="users"
    )

class Account(db.Model):
    __tablename__="accounts"
    account_id:Mapped[int]=mapped_column(Integer,primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey('users.user_id'),nullable=False)
    users:Mapped[List['User']]=relationship(
        back_populates="account"
    )
    favorite:Mapped["Favorite"]=relationship(
        back_populates="account"
    )

class Favorite(db.Model):
    __tablename__="favorites"
    favorite_id:Mapped[int]=mapped_column(Integer,primary_key=True)
    account_id:Mapped[int]=mapped_column(ForeignKey('accounts.account_id'),nullable=False)
    account:Mapped[List['Account']]=relationship(
        back_populates="favorite"
    )
    character_id:Mapped[int]=mapped_column(ForeignKey('characters.character_id'),nullable=False)
    characters:Mapped["Character"]=relationship(
        back_populates="favorities"
    )
    planet_id:Mapped[int]=mapped_column(ForeignKey('planets.planet_id'),nullable=False)
    planets:Mapped["Planet"]=relationship(
        back_populates="favorities"
    )
    vehicle_id:Mapped[int]=mapped_column(ForeignKey('vehicles.vehicle_id'),nullable=False)
    vehicles:Mapped["Vehicle"]=relationship(
        back_populates="favorities"
    )


class Character(db.Model):
    __tablename__="characters"
    character_id:Mapped[int]=mapped_column(Integer,primary_key=True)
    character_name:Mapped[str]=mapped_column(String(250))
    birthday_character:Mapped[str]=mapped_column(String(250))
    favorities:Mapped[List["Favorite"]]=relationship(
        back_populates="characters"
    )

class Planet(db.Model):
    __tablename__="planets"
    planet_id:Mapped[int]=mapped_column(Integer,primary_key=True)
    planet_name:Mapped[str]=mapped_column(String(250))
    planet_name:Mapped[int]=mapped_column(Integer)
    favorities:Mapped[List["Favorite"]]=relationship(
        back_populates="planets"
    )
    
class Vehicle(db.Model):
    __tablename__="vehicles"
    vehicle_id:Mapped[int]=mapped_column(Integer,primary_key=True)
    vehicle_name:Mapped[str]=mapped_column(String(250))
    vehicle_model:Mapped[int]=mapped_column(Integer)
    Favorite:Mapped[List["Favorite"]]=relationship(
        back_populates="vehicles"
    )

