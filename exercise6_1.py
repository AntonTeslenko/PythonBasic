import string

# Ця змінна містить весь латинський алфавіт
alfabet = string.ascii_letters

user_input = input("Enter two letters separated by a hyphen: ")

# Витягуємо першу і другу літеру з введеного рядка
first_user_letter = user_input[0]
second_user_letter = user_input[2]

# Знаходимо індекси першої і другої літери в колекції alfabet
first_index = alfabet.index(first_user_letter)
second_index = alfabet.index(second_user_letter)

# Використовуємо зріз, щоб отримати всі значення між введеними літерами(включно з обома літерами)
result = alfabet[first_index:second_index + 1]

print(result)

# Щоб додатково зробити перевірку на випадок, коли користувач введе, наприклад, "c-a", можемо серед значень індексів
# за допомогою min та max визначити відповідно найменше і найбільше значення
# result = alfabet[min(first_index, second_index):max(first_index, second_index) + 1]


