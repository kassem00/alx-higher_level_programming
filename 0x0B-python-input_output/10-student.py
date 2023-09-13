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
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
