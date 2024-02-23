#!/usr/bin/python3
"""
contains the class definition of a State and an instance 
Base = declarative_base():
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

class State(Base):
    """inherits from Base Tips
    links to the MySQL table states 
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(50)) 
