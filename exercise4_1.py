my_list = [0, 5, 6, True, 0, False, "Hi", -5, 0, 89]

# Новий список з нулями в кінці списку
list_zero = [x for x in my_list if x != 0] + [0] * my_list.count(0)
print(list_zero)
