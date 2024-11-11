def is_even(digit):
    """Перевірка чи є число парним"""
    return digit % 2 == 0


help(is_even)
# Тести для перевірки функції
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

# Можливість користувацького вводу числа для перевірки
user_digit = int(input("Введіть ціле число: "))
if is_even(user_digit):
    print("Число парне.")
else:
    print("Число непарне.")

