def difference(*args):
    """Функція обчислює різницю між мінімальним і максимальним значенням
    у визначеному списку
    Параметри: *args - довільна кількість аргументів
    Повертає: різницю між максимальним і мінімальним значеннями, або 0, якщо
            аргументів немає"""

    if not args:
        return 0
    # Знаходимо максимум і мінімум серед аргументів
    maximum_value = max(args)
    minimum_value = min(args)

    # Повертаємо результат і округлюємо до двох знаків
    return round(maximum_value - minimum_value, 2)

# Тести
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

help(difference)

# Додамо можливість вводу користувачем
users_numbers = input("Введіть числа через пробіл: ")

# Розбиваємо введений рядок за пробілом і перетворюємо кожен елемент у float
#  за допомогою map
numbers = list(map(float, users_numbers.split()))
divide = difference(*numbers)

print(f"Різниця між максимальним значенням і мінімальним = {divide}")