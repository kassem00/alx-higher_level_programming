#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    from sys import argv

    args = argv
    cal = calculator_1

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num1, num2 = int(args[1]), int(args[3])
    opr = {"+": cal.add, "-": cal.sub, "*": cal.mul, "/": cal.div}
    op = args[2]
    
    if op not in list(opr.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("{} {} {} = {}".format(args[1] , op, args[3], opr[op](num1, num2)))
