my_list = [1, 2, -18, "abc", True, 6, False]

# Якщо список порожній, то створимо два порожніх списки
if len(my_list) == 0:
    res = [[], []]
else:
    # Середина списку. Якщо кіль-ть елементів непарна,то перша половина буде більшою
    middle_list = (len(my_list) + 1) // 2

    # Розділення списку на дві половини
    first_list = my_list[:middle_list]
    second_list = my_list[middle_list:]

    # Новий список
    res = [first_list, second_list]

print(res)
