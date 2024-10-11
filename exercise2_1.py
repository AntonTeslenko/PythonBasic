# Просимо користувача ввести 4-значне число
number = int(input("Введіть 4-значне число: "))

# Відокремлюємо кожну цифру за допомогою математичних операцій
number1 = number // 1000
number2 = (number % 1000) // 100
number3 = (number % 100) // 10
number4 = number % 10

# Роздрукуємо цифри в стовпчик
print(number1)
print(number2)
print(number3)
print(number4)
