#!/usr/bin/python3
'''9. class student'''


class Student:
    '''class student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if type(attrs) == list:
            if all(type(element) == str for element in attrs):
                return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student"""
        for m, n in json.items():
            setattr(self, m, n)
