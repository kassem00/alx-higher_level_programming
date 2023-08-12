#!/usr/bin/python3
# 2-args.py
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    import my_fun

    counter = len(sys.argv) - 1

    if counter == 0:
        print("0 arguments.")
    elif counter == 1:
        print("1 argument:")
        my_fun.fun()
    else:
        print("{} arguments:".format(counter))
        my_fun.fun()
