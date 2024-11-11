import re


def first_word(text):
    """ Пошук першого слова """
    # Шукаємо перше слово, яке складається з літер і апострофів
    match = re.match(r"[^\w]*([a-zA-Zа-яА-Я'\-]+)", text)

    # Повертаємо знайдене слово, якщо воно є, якщо ж ні - порожній рядок
    if match:
        return match.group(1)
    return ""


# Тести для перевірки функції
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

user_text = input("Введіть свій рядок: ")
print(first_word(user_text))
