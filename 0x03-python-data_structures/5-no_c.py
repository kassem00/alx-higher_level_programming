#!/usr/bin/python3

def no_c(my_string):
    str_var = '' + my_string
    str_var = my_string.lstrip('c')
    str_var = my_string.lstrip('C')
    return str_var
