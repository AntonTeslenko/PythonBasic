"""Програма дозволяє перетворити рядок на хештег"""

import string

user_string = input("Введіть рядок: ")

# Ініціалізуємо хештег з символу '#'
hashtag = "#"

# Перетворюємо очищений рядок у список
lst = user_string.split()

# Проходимо через кожне слово у списку
for word in lst:
    # Очищене слово
    new_word = ""
    # Проходимо через кожен символ у слові і додаємо до очищеного слова,
    # якщо він не є знаком пунктуації чи пробілом
    for symbol in word:
        if symbol not in string.punctuation and symbol != " ":
            new_word += symbol

    # Додаємо очищене слово до хештегу
    hashtag += new_word.capitalize()

#  Робимо довжину хештегу не більше 140 символів
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)




