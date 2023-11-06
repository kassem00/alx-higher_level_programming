#!/usr/bin/python3
""" class MyList that inherits from list."""


class MyList(list):
    """ class MyList that inherits from list."""

    def print_sorted(self):
        """ that prints the list, but sorted (ascending sort)."""
        print(sorted(self))

        def print_sorted(self, dummy_arg=None):
            """Prints the list sorted in ascending order."""
            raise TypeError("\
            print_sorted() takes 1 positional argument but 2 were given")
