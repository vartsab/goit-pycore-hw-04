def get_cats_info(path: str) -> list:
    """ Функція читає цей файл та повертає список словників 
    з інформацією про кожного кота. """
    # Декларую список для зберігання результатів обробки файла
    cats = []

    # Перевіряю чи такий файл існує за заявленою адресою
    # Для чого відслідковую чи не поверне open FileNotFoundError-помилку
    try:
        with open(path,"r",encoding="utf-8") as file:
            # Перебираю рядки в файлі
            for line in file:
                # Намагаюся розділити рядок на значення розділивши його за комою
                # Результат зберігаю у змінну-список temp
                temp = line.strip().split(",")
                # Якщо структура данних у рядку коректна,
                # формую словник cat
                if len(temp) == 3:
                    cat = {
                        "id": temp[0],
                        "name": temp[1],
                        "age": temp[2]
                    }
                cats.append(cat)
    except FileNotFoundError:
        print("Файл не знайдено!")
        return None
    return cats

cats_info = get_cats_info("cats_file.txt")
print(cats_info)