from options import database

def add():
    # здесь нужно спросить поля и добавить новые данные
    print("Модуль не готов!")
    return

def add_line(id=0, f_name='', s_name='', patr_name='', birth_year='', tel=0, status=''):
    path = database
    with open(path,'a') as data:
        data.write('id:{};f_name:{};s_name:{};patr_name:{};birth_year:{};tel:{};status:{}\n'
        .format(id, f_name, s_name, patr_name, birth_year, tel, status))
    return
