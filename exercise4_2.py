my_list = [3, 5, 6, -4, 5, 6, 9]

# При порожноьому списку результат 0
if len(my_list) == 0:
    res = 0
else:
    # Обчислення суми парних елементів
    my_sum = sum(my_list[i] for i in range(0, len(my_list), 2))
    res = my_sum * my_list[-1]

print(res)