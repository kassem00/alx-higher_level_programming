#!/usr/bin/python3
''' square class module '''
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class module """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new square opject.

        Args:
            width (int): width of new square opject.
            height (int): height of new square opject.
            x (int): Coordinat attribute.
            y (int): Coordinat attribute.
            id (int): id of new square opject.
        """
        super().__init__(size, size, x, y, id)
    
    
    def __str__(self):
        '''[Square] (<id>) <x>/<y> - <size>'''
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
