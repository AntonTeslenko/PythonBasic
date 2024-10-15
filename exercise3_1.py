# Просимо користувача ввести перше число
num1 = float(input("Add the first number: "))

# Просимо користувача ввести операцію над числами
oper = input("Add operation(+, -, *, /: ")

# Просимо користувача ввести друге число
num2 = float(input("Add the second number: "))

match oper:
    case "+":
        res = num1 +num2
        print(f"Result: {res}")
    case "-":
        res = num1 - num2
        print(f"Result: {res}")
    case "*":
        res = num1 * num2
        print(f"Result: {res}")
    case "/":
        if num2 != 0:
            res = num1 / num2
            print(f"Result: {res}")
        else:
            print("Division by zero is impossible!!!")
    case _:
        print("Unknown operation!")