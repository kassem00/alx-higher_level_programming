#!/usr/bin/python3
''' Rectangle class module '''
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class

    Attributes:
        __nb_objects (int): number of opjects created.
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """
        Initialize a new Rectangle opject.

        Args:
            width (int): width of new Rectangle opject.
            height (int): height of new Rectangle opject.
            x (int): Coordinat attribute.
            y (int): Coordinat attribute.
            id (int): id of new Rectangle opject.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        