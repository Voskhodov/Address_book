from options import database

def delete():
    data_for_del = input('Введите данные для удаления в формате: Фамилия;Имя;Отчество.\n'
                         '* При отсутсвии однофамильцев достаточно ввести фамилию ученика: ')
    del_data(data_for_del)


def del_data(data_for_del: str):
    with open(database, 'r', encoding="utf-8") as data:
        lines = data.readlines()
    with open(database, 'w', encoding="utf-8") as data:
        for line in lines:
            if data_for_del not in line:
                data.write(line)
