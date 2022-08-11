from ast import Delete
from json import load
from turtle import width
import Import as ab_import
import Export as ab_export
import Search as ab_search
import add as ab_add
import delete as ab_delete
from tkinter import ttk
import tkinter as tk

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

def fill_data(tree, df):
    tree.delete(*tree.get_children())
    for col in df.columns:
        tree.column(col, anchor='w')
        tree.heading(col, text=col, anchor='w')

    for label, data in df.iterrows():
        tree.insert('', len(tree.get_children()), text=label, values=list(data))

    return

def run_gui():
    def do_command(command, inputValue = ''):
        if (command == 'search'):
            df = ab_import.load()
            #column = str(df.columns[1])
            #s = f'column[1].str.contains("{inputValue}")'
            #print(s)
            #df.query(str, engine='python')
            fill_data(tree, df)
        return

    def do_add():
        return

    def do_delete():
        return

    ws = tk.Tk()
    ws.title('Список пользователей')

    topFrame = tk.Frame(ws)
    topFrame.pack(side='top', ipadx=5, ipady=5, fill='x')
    textSearch=tk.Text(topFrame, height=1, width=100)
    textSearch.pack(side ='left', padx=10)
    buttonSearch=tk.Button(topFrame, height=1, width=10, text="Поиск", command=lambda: do_command('search', textSearch.get("1.0","end-1c")))
    buttonSearch.pack(side ='left', padx=5)
    buttonAdd=tk.Button(topFrame, height=1, width=10, text="Добавить", command=lambda: do_add())
    buttonAdd.pack(side ='left', padx=5)
    buttonRemove=tk.Button(topFrame, height=1, width=10, text="Удалить", command=lambda: do_delete())
    buttonRemove.pack(side ='left', padx=5)

    df = ab_import.load()
    tree = ttk.Treeview(ws, columns=list(df.columns), show='headings', selectmode ='browse')
    tree.config(height=100)
    tree.pack(side ='left')
    vsb = ttk.Scrollbar(ws, orient ='vertical', command=tree.yview) 
    vsb.pack(side='right', fill='y')
    tree.configure(xscrollcommand=vsb.set)
  
    fill_data(tree, df)
    
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
