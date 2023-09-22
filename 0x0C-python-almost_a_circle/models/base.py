#!/usr/bin/python3
''' Base class module '''
import json
import csv

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

    @staticmethod
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
                    dict_lis = []
                    dict_lis.append(ele.to_dictionary())
                    fp.write(Base.to_json_string(dict_lis))

    @staticmethod
    def from_json_string(json_string):
        """
        save dict in beautiful maner list of the
        JSON string representation
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ save dict in beautiful maner """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        fp must be: <Class name>.json
        """
        fp = str(cls.__name__) + ".json"
        try:
            with open(fp, "r") as fjson:
                list_dicts = Base.from_json_string(fjson.read())
                temp = []
                for d in list_dicts:
                    temp.append(cls.create(**d))
                return temp
        except FileNotFoundError:
            return []


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save data to csv file.
        Args:
            list_objs (list): A list ofopjects.
        """
        fp = cls.__name__ + ".csv"
        with open(fp, "w", newline="") as fp_csv:
            if list_objs is None or list_objs == []:
                fp_csv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(fp_csv, fieldnames=["id", "width", "height", "x", "y"])
                if cls.__name__ == "Square":
                    writer = csv.DictWriter(fp_csv, fieldnames=["id", "size", "x", "y"])
                for objects in list_objs:
                    writer.writerow(objects.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """class method read data from a CSV file."""
        fp = cls.__name__ + ".csv"
        try:
            with open(fp, "r", newline="") as fp_csv:
                if cls.__name__ == "Rectangle":
                    list_dicts = csv.DictReader(fp_csv, fieldnames= ["id", "width", "height", "x", "y"])
                if cls.__name__ == "Square":
                    list_dicts = csv.DictReader(fp_csv, fieldnames= ["id", "size", "x", "y"])
                list_dicts = []
                for d in list_dicts:
                    new_dict = {}
                    for k, v in d.items():
                        new_dict[k] = int(v)
                    list_dicts.append(new_dict)

                result = []
                for d in list_dicts:
                    obj = cls.create(**d)
                    result.append(obj)
                return result        
        except FileNotFoundError:
            return []
