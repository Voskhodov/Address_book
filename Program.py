import Import as ab_import
import Export as ab_export
import Search as ab_search
import add as ab_add
import delete as ab_delete

from options import database

def load():
    return ab_import.load_data(database)

def save(data):
    return ab_export.save_data(database, "csv", data)

def list_data():
    data = load()
    print(data.to_string())
    return

commands = {
    "1": list_data,
    "2": ab_search.search,
    "3": ab_add.add,
    "4": ab_delete.delete,
    "5": ab_import.import_data,
    "6": ab_export.export_data,
}

def run():
    while True:
        print("Что вы ходите сделать:")
        print("1. Вывести список учеников")
        print("2. Искать ученика")
        print("3. Добавить нового ученика")
        print("4. Удалить ученика")
        print("5. Импортировать список учеников из CSV файла")
        print("6. Экспортировать список учеников в файл (" + ", ".join(ab_export.supported_export) + ")")
        print("q. Выход")
        mode = input()
        if mode in list("123456q"):
            if mode == "q":
                break
            commands[mode]()
    
    return
