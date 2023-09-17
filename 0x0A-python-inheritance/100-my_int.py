#!/usr/bin/python3

"""Defines a class"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
