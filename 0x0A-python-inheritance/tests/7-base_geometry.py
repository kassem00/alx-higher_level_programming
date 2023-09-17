=============================
How to Use 7-base_geometry.py
=============================

class BaseGeometry (based on 6-base_geometry.py).

Instantiation
=============

``BaseGeometry`` with no arguments.

::

    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
    >>> bg = BaseGeometry()
    >>> type(bg)
    <class '7-base_geometry.BaseGeometry'>

::

    >>> print(bg) # doctest: +ELLIPSIS
    <7-base_geometry.BaseGeometry object at ...>

::

    >>> bg = BaseGeometry(None)
    Traceback (most recent call last):
    TypeError: object() takes no parameters

Methods
=======

implemented.

::

    >>> bg = BaseGeometry()
    >>> print(bg.area)
    <bound method BaseGeometry.area of <7-base_geometry.BaseGeometry 
     object at...>>

::

    >>> bg.area()
    Traceback (most recent call last):
    Exception: area() is not implemented

::

    >>> print(bg.integer_validator) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    <bound method BaseGeometry.integer_validator of <7-base_geometry.BaseGeometry 
    object at...>>

::


   >>> bg.integer_validator("valid number", 1)

::

    >>> bg.integer_validator("invalid number", "number")
    Traceback (most recent call last):
    TypeError: invalid number must be an integer

::

    >>> bg.integer_validator("another invalid", True)
    Traceback (most recent call last):
    TypeError: another invalid must be an integer

::

    >>> bg.integer_validator("invalid tuple", (0,))
    Traceback (most recent call last):
    TypeError: invalid tuple must be an integer

::

    >>> bg.integer_validator("and another", [2])
    Traceback (most recent call last):
    TypeError: and another must be an integer

::

    >>> bg.integer_validator("more invalid testing", {32, 54})
    Traceback (most recent call last):
    TypeError: more invalid testing must be an integer

::

    >>> bg.integer_validator("absolutely every possible invalid", None)
    Traceback (most recent call last):
    TypeError: absolutely every possible invalid must be an integer

::

    >>> bg.integer_validator("invalid int", -2)
    Traceback (most recent call last):
    ValueError: invalid int must be greater than 0

::

    >>> bg.integer_validator("invalid int", 0)
    Traceback (most recent call last):
    ValueError: invalid int must be greater than 0

::

    >>> bg.integer_validator() # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: integer_validator() missing 2 required positional arguments: 
    'name' and 'value'

::

    >>> bg.integer_validator(None) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: integer_validator() missing 1 required positional argument: 
    'value'

::

    >>> bg.integer_validator({"a": 1}, (1, 2))
    Traceback (most recent call last):
    TypeError: {'a': 1} must be an integer
