#!/usr/bin/python3
''' Base class module '''
import json


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
    def to_json_string(list_dictionaries):
        '''standard formats for sharing data'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
