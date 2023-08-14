import hidden_4

def print_all_names():
    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)

if name == "main":
    """Print all names defined by hidden_4 module."""
    print_all_names()
