from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = ["+", "-", "*", "/"]

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# print(operations["*"](4, 8))

def calculator(num):

    for symbol in operations:
        print(symbol)
    operator = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    if operator == "+":
        num3 = add(num, num2)

    elif operator == "-":
        num3 = subtract(num, num2)

    elif operator == "*":
        num3 = multiply(num, num2)

    elif operator == "/":
        num3 = divide(num, num2)

    return num3





# while use_calc:
#     output = calculator(num1)
#     print(output)
#
#     should_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()
#     if should_continue == "y":
#         calculator(calculator(num1))
#     elif should_continue == "n":
#         break

num1 = float(input("What's the first number? "))



def wanna_play_again(num):
    output = calculator(num)
    print(f"The result is: {output}")
    should_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()
    if should_continue == "y":

        wanna_play_again(output)
    elif should_continue == "n":
        print("\n" * 100)
        wanna_play_again(float(input("What's the first number? ")))


wanna_play_again(num1)
