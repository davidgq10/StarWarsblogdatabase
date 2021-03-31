import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    mail = Column(String(100), nullable=False)
    password = Column(String(15), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table character.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(15), nullable=True)
    hair_color = Column(String(100), nullable=True)
    eyes_color = Column(String(30), nullable=True)
    birth_year = Column(String(10), nullable=False)
    height = Column(Integer, nullable = False)
    skin_color = Column(String(100),nullable=True)
    description = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table planet.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String (250),nullable=False)
    population = Column(Integer,nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String)
    orbital_period = Column(Integer)
    rotacion_period = Column(Integer)
    diameter = Column (Integer, nullable = False)
    description = Column(String)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table favorite.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    type_favorite = Column(Integer,nullable = False)
    relationship_id = Column(Integer,nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')