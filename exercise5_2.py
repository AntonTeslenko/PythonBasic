"""Модифікована програма калькулятора дозволить йому працювати доти, доки цього
   хоче користувач. Якщо користувач не виявить бажання продовжувати обчислення,
   то калькулятор припинить свою роботу"""

while True:

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

    # Робимо запит від користувача, чи хоче він продовжити роботу
    continue_calc = input("Do you want to continue? (yes): ")
    if continue_calc not in ["yes"]:
        print("STOP!")
        break