"""Програма дозволяє перетворити рядок на хештег"""

import string

user_string = input("Введіть рядок: ")

# Створюємо очищений рядок
final_string = ""

# Створюємо хештег
hashtag = "#"

# Проходимо кожен символ введеного рядка і перевіряємо,
# чи не є символ пробілом чи знаком пунктуації
for symbol in user_string:
    if symbol not in string.punctuation:
         final_string += symbol

# Перетворюємо очищений рядок у список
new_string = final_string.split()

#  Для створення хештегу
for word in new_string:
    hashtag += "".join(word.capitalize())

#  Робимо довжину хештегу не більше 140 символів
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)




