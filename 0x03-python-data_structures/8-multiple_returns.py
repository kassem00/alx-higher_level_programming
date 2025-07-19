#!/usr/bin/python3


def multiple_returns(sentence):
    """
    function that returns a tuple with the
    length of a string and its first character.
    """
    if sentence:
        return (len(sentence), sentence[0])
    return ()
