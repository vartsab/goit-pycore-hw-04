def total_salary(path: str) -> tuple[int, float]:
    # Декларую три локальні змінні для збереження результатів обробки файлу
    total = 0
    count = 0
    temp = []

    # Перевіряю чи такий файл існує за заявленою адресою
    # Для чого відслідковую чи не поверне open FileNotFoundError-помилку
    try:
        with open(path, "r", encoding="utf-8") as file:
            # Перебираю рядки в файлі
            for line in file:
            # Намагаюся розділити рядок на значення розділивши його за комою
            # Результат зберігаю у змінну-список temp
                temp = line.strip().split(",")
                # Дані у файлі має бути збережено у форматі <Ім'я>, <Зарплата>
                # Якщо структура данних у рядку коректна, обробляю дані
                if len(temp) == 2:
                    total += int(temp[1])
                    count += 1

    # Виводжу повідомлення, якщо файл не знайдено, так виходжу із функції
    except FileNotFoundError:
        print("Файл не знайдено!")
        return None

    # Виводжу повідомлення якщо файл не містить даних
    if count == 0:
        print("Файл пустий або пошкоджений!")
        return None

    return total, total / count

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}," \
      f" Середня заробітна плата: {average}")
