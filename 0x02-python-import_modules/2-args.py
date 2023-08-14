#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    '''
    Number of argument(s) followed by argument
    (if number is one) or arguments (otherwise), followed by
    : (or . if no arguments were passed) followed by
    a new line, followed by (if at least one argument),
    one line per argument:
    the position of the argument (starting at 1) followed by :,
    followed by the argument value and a new line
    '''
    num_args = len(argv) - 1
    print("{} argument{}".format(num_args, 's' if num_args != 1 else ''),
          end='')
    if num_args == 0:
        print(".")
    else:
        print(':')
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
