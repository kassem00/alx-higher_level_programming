#!/usr/bin/python3
''' Base class module '''


class Base:
    """
    This class will be the “base” of all other classes

    Attributes:
        __nb_objects (int): number of opjects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
      """
      Initialize a new Base opject.

      Args:
          id (int): id of new Base opject.
      """
      if id == None:
          Base.__nb_objects += 1
          self.id = Base.__nb_objects
      else:
          self.id = id
