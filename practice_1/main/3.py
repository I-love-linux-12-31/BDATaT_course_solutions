def _add(a, b):
    return a + b

def _subtract(a, b):
    return a - b

def _multiply(a, b):
    return a * b

def _divide(a, b):
    return a / b

def _div(a, b):
    return a // b

def _power(a, b):
    return a ** b

def _abs(a, b):
    return abs(a), abs(b)

def bad_input_msg():
    print("Bad operation!")

operations = {
    "+": _multiply,
    "-": _divide,
    "*": _multiply,
    "/": _divide,
    "//": _div,
    "div": _div,
    "**": _power,
    "pow": _power,
    "abs": _abs,
}

def main():
    print("enter 2 numbers and operation in one line:")
    a, b, op = input().split()
    function = operations.get(op, bad_input_msg)
    print(F"Result of operation '{op}' is: {function(int(a), int(b))}")


if __name__ == '__main__':
    main()
