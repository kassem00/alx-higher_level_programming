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
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        standard formats for sharing data
        Args:
            list_dictionaries (list): dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ save dict in beautiful maner """
        name = cls.__name__ + ".json"
        with open(name, "w") as fp:
            if list_objs is None:
                fp.write("[]")
                return
            else:
                for ele in list_objs:
                    dict_lis =[]
                    dict_lis.append(ele.to_dictionary())
                    fp.write(Base.to_json_string(dict_lis))