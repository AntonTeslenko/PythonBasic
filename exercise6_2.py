"""Програма дозволить переводити кількість секунд
    у формат часу у читальному вигляді"""

seconds = int(input("Введіть кількість секунд від 0 до 8640000: "))

# Перевіряємо, чи введене число попадає у потрібний діапазон
if 0 <= seconds <= 8640000:
    # Кількість днів
    days, other_seconds = divmod(seconds, 86400)  #other_seconds-кількість секунд після ділення

    # Кількість годин
    hours, other_seconds = divmod(other_seconds, 3600)

    # Кількість хвилин
    minutes, other_seconds = divmod(other_seconds, 60)

    # Секунди, що залишились
    other_seconds = other_seconds

    # Робимо перевірку, щоб слово "день" підбиралося на основі кількості днів
    if days % 10 == 1 and days != 11:
         days_format = "день"
    elif days % 10 in [2, 3, 4] and days not in [12, 13, 14]:
         days_format = "дні"
    else:
        days_format = "днів"

    # Приводимо години, хвилини і секунди до формату "00:00:00"
    hours_format = str(hours).zfill(2)
    minutes_format = str(minutes).zfill(2)
    seconds_format = str(other_seconds).zfill(2)

    print(f"{seconds} ==> {days} {days_format}, {hours_format}:{minutes_format}:{seconds_format}")
else:
    print("Введіть число в діапазоні від 0 до 8640000!")

