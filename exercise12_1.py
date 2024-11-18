import re
import codecs


def delete_html_tags(html_file, result_file = 'cleaned.txt'):
    """
    Функція очищує текст від HTML-тегів і записує результат в інший файл.
    :param html_file: Шлях до HTML-файлу, який потрібно очистити.
    :param result_file: Шлях до файлу, куди потрібно записати очищенний результат.
    """
    try:
        # Прочитаємо вхідний файл
        with codecs.open(html_file, 'r', 'UTF-8') as file:
            html_content = file.read()

        # Видалення тегів за допомогою регулярного виразу
        text_without_tags = re.sub(r'<[^>]*>', '', html_content)

        # Запис у файл результату
        with codecs.open(result_file, 'w', 'UTF-8') as output_file:
            output_file.write(text_without_tags)

        print(f"Файл {html_file} очищено і збережено {result_file}")

    except FileNotFoundError:
        print(f"Файл {html_file} не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}!")


delete_html_tags('draft.html', 'my_cleaned_file.txt')