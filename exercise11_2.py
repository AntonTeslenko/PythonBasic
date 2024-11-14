from inspect import isgenerator

def generate_cube_numbers(end):
    start_number = 2 # Початкове значення
    while True:
        calculate_cube = start_number ** 3
        if calculate_cube > end:
            return # Якщо значення кубу більше за кінцеве значення, виходимо з генератора
        yield calculate_cube # Повертаємо куб
        start_number  += 1 # Збільшуємо початкове значення на 1 для наступної ітерації

# Тестування функції
gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('Ok')
