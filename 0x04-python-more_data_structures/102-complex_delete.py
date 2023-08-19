#!/usr/bin/python3

def complex_delete(a_dictionary, value):
  new_dictionary = {}

  for k, v in a_dictionary.items():
      if v != value:
          new_dictionary[k] = v
    return new_dictionary
