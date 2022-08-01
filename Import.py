import pandas as pd
from options import database
import Export as ab_export

# загрузка данных
# читаем CSV файл, возвращаем DataFrame
# нет обработки ошибок
def load_data(filename):
    return pd.read_csv(filename, sep=";")

# импорт
# 1) зачитываем текущую базу
# 2) добавляем новые данные (вопрос: нужна проверка на дубликаты?)
# 3) при добавлении создаем новый уникальный id
# 4) сохраняем в текущую базу 
def import_file(filename):
    db = load_data(database)
    imported = load_data(filename)
    max_id = db["id"].max() + 1
    imported['id'] = range(max_id, max_id+len(imported))
    result = pd.concat([db, imported])
    return ab_export.save_data(database, "csv", result)