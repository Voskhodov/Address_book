from json import load
import Import as ab_import
import Export as ab_export
import Search as ab_search
import add as ab_add
import delete as ab_delete
from tkinter import ttk
import tkinter

from options import database

def list_data():
    data = ab_import.load()
    print(data.to_string())
    return

commands = {
    "1": list_data,
    "2": ab_search.search,
    "3": ab_add.add,
    "4": ab_delete.delete,
    "5": ab_import.importf,
    "6": ab_export.export_data,
}

def run_gui():
    ws = tkinter.Tk()
    ws.title('Список пользователей')

    df = ab_import.load()
    columns = list(df.columns)
    tree = ttk.Treeview(ws, columns=columns, show='headings', height=5)
    tree.pack(fill='both', expand='yes')

    tree['columns'] = columns
    for col in columns:
        tree.column(col, anchor='w')
        tree.heading(col, text=col, anchor='w')

    for label, data in df.iterrows():
        tree.insert('', len(tree.get_children()), text=label, values=list(data))

    # style = ttk.Style()
    # style.theme_use("default")
    # style.map("Treeview")

    ws.mainloop()

    return

def run_console():
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
