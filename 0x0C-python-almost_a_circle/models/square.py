#!/usr/bin/python3
''' square class module '''
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class module """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new square opject.

        Args:
            size (int): size of new square opject.
            x (int): Coordinat attribute.
            y (int): Coordinat attribute.
            id (int): id of new square opject.
        """
        super().__init__(size, size, x, y, id)
    
    
    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """property of height"""
        return self.height

    @size.setter
    def size(self, value):
        """setter of height"""
        self.width = value
        self.height = value
