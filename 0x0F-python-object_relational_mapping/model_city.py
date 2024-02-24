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


class City(Base):
    """city for a MySQL database"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
