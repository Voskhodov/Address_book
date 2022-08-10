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
    def do_search():
        inputValue=textSearch.get("1.0","end-1c")
        print(inputValue)

    ws = tkinter.Tk()
    ws.title('Список пользователей')

    searchFrame=tkinter.Frame(ws)
    searchFrame.pack(fill='both')
    textSearch=tkinter.Text(searchFrame, height=1, width=100)
    textSearch.pack(side='left', fill='both', expand='yes', padx=10, pady=5)
    buttonSearch=tkinter.Button(searchFrame, height=1, width=10, text="Поиск", command=lambda: do_search())
    buttonSearch.pack(side='right', padx=15, pady=5)

    mainFrame=tkinter.Frame(ws)
    mainFrame.pack(fill='both', expand='yes')

    df = ab_import.load()
    columns = list(df.columns)
    tree = ttk.Treeview(mainFrame, columns=columns, show='headings', height=10)
    tree.pack(fill='both', expand='yes')

    buttonFrame=tkinter.Frame(mainFrame)
    buttonFrame.pack(side='right')
    buttonAdd=tkinter.Button(buttonFrame, height=1, width=10, text="Добавить", command=lambda: do_search())
    buttonAdd.pack(side='bottom', padx=15, pady=5)
    buttonRemove=tkinter.Button(buttonFrame, height=1, width=10, text="Удалить", command=lambda: do_search())
    buttonRemove.pack(side='bottom', padx=15, pady=5)

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
