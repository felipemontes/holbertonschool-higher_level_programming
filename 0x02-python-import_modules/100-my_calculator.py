#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    var1 = int(sys.argv[1])
    var2 = int(sys.argv[3])
    oper = sys.argv[2]
    if len(sys.argv) is not 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif oper == "+":
        print("{} + {} = {}".format(var1, var2, calc.add(var1, var2)))
    elif oper == "-":
        print("{} - {} = {}".format(var1, var2, calc.sub(var1, var2)))
    elif oper == "*":
        print("{} * {} = {}".format(var1, var2, calc.mul(var1, var2)))
    elif oper == "/":
        print("{} / {} = {}".format(var1, var2, calc.div(var1, var2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
