def is_palindrome(text):
    # Пустий список для зберігання після "очищення"
    cleand_list = []

     # Проходимо по кожному символу в тексті
    for symbol in text:

        # Перевірка, чи є символ буквою або цифрою
        if symbol.isalnum():

            # Якщо символ алфавітно-цифровий, переводимо його в нижній регістр і додаємо до списку
            cleand_list.append(symbol.lower())

    # Об'єднуємо символи списку в один рядок
    cleand_text = ''.join(cleand_list)

    # Перевіряємо, чи є очищений текст паліндромом
    return cleand_text == cleand_text[::-1]

 # Тестування функції
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

# Можливість вводу з клавіатури виразу, який будемо перевіряти
user_text = input("Enter a string to check for a palindrome: ")
if is_palindrome(user_text):
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")