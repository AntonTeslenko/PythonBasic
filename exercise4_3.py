import random

# Генеруємо список згідно заданих умов
my_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]

# Список з першим, третім і другим з кінця елементами
final_list = [my_list[0], my_list[2], my_list[-2]]
print(my_list)
print(final_list)