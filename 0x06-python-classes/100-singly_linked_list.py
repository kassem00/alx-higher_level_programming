#!/usr/bin/python3
'print(__import__("my_module").my_function.__doc__)'


class Node:
    'print(__import__("my_module").my_function.__doc__)'
    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) != int and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
