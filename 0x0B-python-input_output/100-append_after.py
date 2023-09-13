#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file."""
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w") as file:
        file.writelines(lines)
