def common_elements():
    # За допомогою генератора списків генеруємо множину чисел, кратних 3
    numbers_three = {x for x in range(100) if x % 3 == 0}

    # Генеруємо множину чисел, кратних 5
    numbers_five = {x for x in range(100) if x % 5 == 0}

    # За допомогою операції перетину знаходимо спільні елементи
    elements = numbers_five & numbers_three

    return elements

# Перевірка правильності результату
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Результат:", common_elements())