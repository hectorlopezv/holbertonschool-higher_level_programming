#!/usr/bin/python3
"""how to use mysql client and compare it so sql alchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Column, String, ForeignKey, Integer
from model_state import Base, State


class City(Base):
    """state class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state_ = relationship('State', backref='state', cascade='all, delete')
