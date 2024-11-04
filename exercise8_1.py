def add_one(some_list) -> list:

    # Цей цикл проходить по індексах елементів some_list з кінця до початку
    for i in range(len(some_list) - 1, -1, -1):

        # Додаємо 1 до останньої цифри, якщо вона > 9
        if some_list[i] < 9:
            some_list[i] += 1
            return some_list  # Повертаємо список, якщо не потрібен перенос

        # Якщо цифра була 9, ставимо її в 0 і продовжуємо цикл
        some_list[i] = 0
    # Якщо ж весь список був 9, додаємо 1 на початок
    return [1] + some_list

# Тестування функції
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

# Просимо користувача ввести число з клавіатури
user_list = input("Enter digit: ")

# Перетворюємо рядок у список цілих чисел (цифр)
some_list = [int(digit) for digit in user_list]

result = add_one(some_list)
print(result)