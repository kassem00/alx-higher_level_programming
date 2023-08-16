#!/usr/bin/python3

def no_c(my_string):
    str_var = '' + my_string
    str_var = my_string.lstrip('c')
    str_var = my_string.lstrip('C')
    str_var = my_string.strip('c')
    str_var = my_string.strip('C')
    return str_var
