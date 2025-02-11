import pandas as pd
import os

# Спрашиваем у пользователя, какие столбцы нужны
columns_needed = input("Какие столбцы из таблицы ты хочешь оставить? (Перечисли через запятую): ")
columns_needed = [col.strip() for col in columns_needed.split(",")]

# Спрашиваем у пользователя, где лежит файл с таблицей
file_path = input("Где находится файл с этой таблицей? (Укажите путь к файлу): ")

# Проверяем, есть ли такой файл
if not os.path.exists(file_path):
    print("Файл не найден. Пожалуйста, проверьте путь к файлу.")
else:
    # Загружаем таблицу
    df = pd.read_csv(file_path)

    # Проверяем, все ли столбцы на месте
    for col in columns_needed:
        if col not in df.columns:
            df[col] = None  # Добавляем пустой столбец, если его нет

    # Оставляем только нужные столбцы
    df = df[columns_needed]

    # Сохраняем новую таблицу
    new_file_path = file_path.replace(".csv", "_re.csv")
    df.to_csv(new_file_path, index=False)

    # Готово!
    print(f"Работа завершена! Новый файл сохранен по пути: {new_file_path}")