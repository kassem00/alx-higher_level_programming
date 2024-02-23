#!/usr/bin/python3
"""
contains the class definition of a State and an instance 
Base = declarative_base():
"""
from sqlalchemy import create_engine, String, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
import time

Base = declarative_base()


class State(Base):
    """inherits from Base Tips
    links to the MySQL table states 
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False) 
