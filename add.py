from options import database

id=0
# f_name=''
# s_name=''
# patr_name=''
# birth_year=''
# tel=0
# status=''

def add():
    # здесь нужно спросить поля и добавить новые данные. Добавлено
    # id = max(for id in len(str)) + 1 # как задать id?
    f_name = input("Введите фамилию: ")
    s_name = input("Введите имя: ")
    patr_name = input("Введите отчество: ")
    birth_year = input("Введите год рождения: ")
    tel = input("Введите телефон: ")
    status = input("Введите статус: ")
    print('Добавили запись: {};{};{};{};{};{};{}'.format(id, f_name, s_name, patr_name, birth_year, tel, status))
    path = database
    with open(path,'a', encoding="utf-8") as data:
        data.write('{};{};{};{};{};{};{}\n'
        .format(id, f_name, s_name, patr_name, birth_year, tel, status))
    return

add()
# def add_line():
#     path = 'fio1.csv'
#     with open(path,'a') as data:
#         data.write('id:{};f_name:{};s_name:{};patr_name:{};birth_year:{};tel:{};status:{}\n'
#         .format(id, f_name, s_name, patr_name, birth_year, tel, status))
#     return
