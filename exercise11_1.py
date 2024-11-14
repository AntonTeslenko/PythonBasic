from inspect import isgenerator


def prime_generator(end):
    """
    Функція-генератор, яка повертатиме прості числа
    :param end:Верхня межа цього діапазону
    :return: повертатиме список простих чисел
    """

    # Вкладена функція для перевірки, чи є число n простим
    def is_prime(n):
        if n < 2:
            return False  # Бо числа меньше 2 не є простими

        # Перевірка, чи ділиться n на будь-яке число від 2 до кореня квадратного з n
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False  # Якщо знайдено дільник, то n не є простим числом
        return True  # Повертаємо число, якщо дільник не знайдено, то n - просте

    # Генеруємо числа від 2 до заданої межі end
    for num in range(2, end + 1):

        # Для перевірки чи число просте використовуємо вкладену функцію
        if is_prime(num):
            yield num  # Якщо число просте - повертаємо його


help(prime_generator)

# Тести для перевірки
gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

# Користуваацький ввод
try:
    end = int(input("Введіть верхню межу для генерації простих чисел: "))
    if end < 2:
        print("Введіть число більше, або рівне 2!")
    else:
        generator = list(prime_generator(end))
        print(f"Прості числа до {end}: {generator}")
except ValueError:
    print("Введіть ціле число!")
