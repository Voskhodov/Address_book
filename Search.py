import pandas as pd
import matplotlib.pyplot as plt
from options import database
import csv
from Program import list_data




def search():
name = list(input('Введите Фамилию или Имя для поиска: '))
    with open('fio.csv', 'r', encoding='utf-8') as f:
        search_data = csv.DictReader(f, str)
        for row in search_data:
            if name in row:
                print(row)
            else:
                print("По заданным параметрам ничего не найдено")
                return search
    
    return list_data

# search(name)
