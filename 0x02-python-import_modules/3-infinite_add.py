#!/usr/bin/python3
# 2-args.py
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    temp = 0
    counter = len(sys.argv) - 1

    if counter == 1:
        print("0")
    else:
        for i in range(len(sys.argv)):
            if i > 0:
                temp = temp + int(sys.argv[i])

    print(f"{temp}")
