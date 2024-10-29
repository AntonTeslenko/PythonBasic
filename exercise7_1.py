def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

# Перевірка функціЇ
assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

# Просимо користувача ввести ім'я та вік
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(say_hi(user_name, user_age))

