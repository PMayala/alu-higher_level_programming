#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    sym = ["+", "-", "*", "/"]

    for i in range(len(sym)):
        if sym[i] == "+":
            res = add(a, b)
        if sym[i] == "-":
            res = sub(a, b)
        if sym[i] == "*":
            res = mul(a, b)
        if sym[i] == "/":
            res = div(a, b)
        print("{0} {1} {2} = {3}".format(a, sym[i], b, res))
