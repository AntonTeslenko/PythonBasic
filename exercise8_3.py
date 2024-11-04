def find_unique_value(some_list):
    # Створюємо множину з усіх чисел у списку
    unique_numbers = set(some_list)

    # "Проходимо" циклом по кожному числу з множини
    for number in unique_numbers:
        # Якщо кількість входжень числа = 1, повертаємо його
        if some_list.count(number) == 1:
            return number

# Тестування функції
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

# Додамо можливість вводу з клавіатури
user_list = input("Ввести список чисел, розділених комою: ")
some_list = [int(number) for number in user_list.split(',')]
unique_value = find_unique_value(some_list)
print(f"Унікальне число: {unique_value}")
