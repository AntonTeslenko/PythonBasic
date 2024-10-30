def second_index(text: str, some_str: str):
    # Знайдемо індекс першого входження шуканого підрядка
    first_index = text.find(some_str)

    # Якщо перше входження не буде знайдено, то функція повертає None
    if first_index == -1:
        return None

    # Знайдемо індекс другого входеження шуканого підрядка
    second_index = text.find(some_str, first_index + len(some_str))

    # Якщо друге входження буде знайдено - повертаємо індекс, якщо ні - None
    if second_index != -1:
        return second_index
    else:
        return None


# Тести для перевірки
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

# Просимо користувача ввести текст і рядок для пошуку
user_text = input("Enter text: ")
user_some_str = input("Enter search string: ")

print(f"Index of the search string: {second_index(user_text, user_some_str)}")
