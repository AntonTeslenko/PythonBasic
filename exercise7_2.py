def correct_sentence(text):
    text = text[0].upper() + text[1:]  # "Капіталізуємо" першу літеру
    if text[-1] != ".":  # Якщо останній символ не ".", то додаємо крапку в кінці
        text += "."
    return text

# Робимо тести для нашої функції
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

# Просимо користувача ввести текст
user_text = input("Enter your text: ")
print(f"Correct sentence is: {correct_sentence(user_text)}")