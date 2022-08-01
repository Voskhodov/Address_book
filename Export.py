import pandas as pd
import Import as ab_import
from options import database

# сохранение строки в файл
def write_file(target, str):
    with open(target, "w", encoding="utf-8") as f:
        return f.write(str)

# запись данных DataFrame в файл
# mode: csv, excel, html, json, text
# нет обработки ошибок
def save_data(target, mode, data: pd.DataFrame):
    if mode == "csv":
        return data.to_csv(target, index=False, sep=";")
    if mode == "excel":
        return data.to_excel(target, index=False)
    if mode == "html":
        return write_file(target, data.to_html(index=False))
    if mode == "json":
        return write_file(target, data.to_json())
    if mode == "text":
        return write_file(target, data.to_string(index=False))

# экспорт текущей базы в файл
# зачитываем текущую базу
# экспортируем в другой формат
# mode: csv, excel, html, json, text
def export_file(target, mode):
    df = ab_import.load_data(database)
    return save_data(target, mode, df)