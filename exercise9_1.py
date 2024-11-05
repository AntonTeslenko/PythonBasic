def popular_words(text, words):
    """Функція підраховує кількість вказаних слів у тексті.
    Параметри: text - вхідний текст, в якому підраховується кількість шуканих слів
               words - список слів, кількість яких треба підрахувати
    Повертає: словник, де ключі - слова зі списку, а значення - їх кількість
    """
    # Приводимо весь текст до нижнього регістру та приводимо до списку
    text = text.lower().split()

# Словник, в якому підрахуємо кількість слів
    dictionary_quantity = {word: text.count(word) for word in words}

    return dictionary_quantity

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

# Можливість вводу тексту користувачем
user_text = input("Ввести текст: ")
user_words = input("Ввести шукані слова через пробіл: ").split()

help(popular_words)
print(popular_words(user_text, user_words))