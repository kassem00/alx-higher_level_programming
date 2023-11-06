#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None:
        c = sorted(a_dictionary.values())
        big = c[-1:]
        for k in a_dictionary.keys():
            if big == a_dictionary[k]:
                return k
