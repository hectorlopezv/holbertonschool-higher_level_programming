#!/usr/bin/python3
"""how to use mysql client and compare it so sql alchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
Base = declarative_base()  # used to make classes a table.....fml


class State(Base):
    """state class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref=backref('state', cascade='all, delete'), single_parent=True)
