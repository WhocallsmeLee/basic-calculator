def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Cannot divide by 0")
        return None
    else:
        return n1 / n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


def calculator():
    calculate = True
    new_calculation = True
    value = 0
    while calculate:
        if new_calculation:
            first_number = float(input("What is the first number?: "))
        else:
            first_number = value
        print("+\n-\n*\n/")
        symbol = input("Pick an operation: ")
        while symbol not in operations:
            print("Invalid operation. Please pick from +, -, *, /")
            symbol = input("Pick an operation: ")
        second_number = float(input("What is the next number?: "))
        value = operations[symbol](first_number,second_number)
        if value is not None:
            print(f"{first_number} {symbol} {second_number} = {value}")
        keep_calculating = input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation, or type 'exit' to exit calculator: ").lower()
        if keep_calculating == "y":
            new_calculation = False
        elif keep_calculating == "n":
            print("\n" * 100)
            new_calculation = True
            value = 0
        elif keep_calculating == "exit":
            print("Exiting calculator!")
            calculate = False
        else:
            print("Did not pick correct input")
            break



calculator()