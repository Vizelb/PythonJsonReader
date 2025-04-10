import pandas as pd
import json
import os
from tkinter import Tk, filedialog, messagebox
import serial
import time

# Скрыть главное окно
root = Tk()
root.withdraw()

# Выбор Excel-файла
file_path = filedialog.askopenfilename(
    title="Выберите Excel-файл",
    filetypes=[("Excel files", "*.xlsx *.xls")]
)

if not file_path:
    messagebox.showinfo("Отмена", "Файл не выбран.")
    exit()

try:
    df = pd.read_excel(file_path)

    # Проверка, что нужные колонки существуют
    if not {'name', 'city', 'age'}.issubset(df.columns):
        raise ValueError("Файл должен содержать столбцы: name, city, age")

    grouped = {}

    for _, row in df.iterrows():
        name = row['name']
        city = row['city']
        age = row['age']

        entry = {'city': city, 'age': age}

        if name in grouped:
            grouped[name].append(entry)
        else:
            grouped[name] = [entry]

    # Сохранение JSON
    json_path = os.path.splitext(file_path)[0] + "_grouped.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(grouped, f, ensure_ascii=False, indent=4)

    messagebox.showinfo("Успех", f"Группированный JSON сохранён как:\n{json_path}")

except Exception as e:
    messagebox.showerror("Ошибка", f"Что-то пошло не так:\n{e}")
