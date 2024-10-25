# Просимо користувача ввести ціле число
user_number = int(input("Enter an integer: "))

# Допоки user_number>9-->True, розбиваємо його і перемножуємо цифри
while user_number > 9:
    some_variable = 1  # Створюємо змінну, в якій будемо зберігати результат множення цифр
    for numeric in str(user_number):  # Перетворюємо назад цифру у рфдок, щоб "пройтись" по кожній цифрі
        some_variable *= int(numeric)  # Знову робимо перетворення у число для перемноження
    user_number = some_variable  # Записуємо результат дій у user_number

print(f"Calculation result is: {user_number}")
