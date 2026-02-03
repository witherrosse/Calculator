#calculator my chalnage
#add functions to do the operators
def plus(num1,num2):
    return num1 + num2
def minus(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2
def power(num1,num2):
    return num1 ** num2
def mod(num1,num2):
    return num1 % num2
operations = {
    "+": plus,
    "-": minus,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": mod
}
should_continue = True
first_number = float(input("Enter first number: "))
while should_continue:
    next_number = float(input("Enter next number: "))
    operator = input("chose youre operation '+' '-' '*' '/' '^' '%' : ")

    if operator in operations:
        operation = operations[operator]
        result = operation(first_number, next_number)
        print(result)
    else:
        print("Invalid operation")
    want_more = input("press 'y' to continue and press 'q' to quit")
    if want_more == "y":
        first_number = result
    elif want_more == "q":
        should_continue = False
    else:
        print("Invalid key")