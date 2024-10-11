# Просимо користувача ввести 5-значне число
number = int(input("Введіть 5-значне число: "))

# Відокремлюємо кожну цифру за допомогою математичних операцій
number1 = number % 10
number = number // 10

number2 = number % 10
number = number // 10

number3 = number % 10
number = number // 10

number4 = number % 10
number = number // 10

number5 = number % 10
number = number // 10

# Формування перевернутого числа
revers_number = number1 * 10000 + number2 * 1000 + number3 * 100 + number4 * 10 + number5
print(revers_number)
