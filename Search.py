import pandas as pd
from options import database
import csv


def search():

    name = str(input('Введите Фамилию или Имя для поиска: '))
    with open(database, 'r', encoding='utf-8') as data:
        lines = data.readlines()
        for line in lines:
            if name in line:
                print(line)
            else:
                print("По заданным параметрам ничего не найдено")
                continue
