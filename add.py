def add_line(id=0, f_name='', s_name='', patr_name='', birth_year='', tel=0, status=''):
    path = 'fio.csv'
    with open(path,'a') as data:
        data.write('id:{};f_name:{};s_name:{};patr_name:{};birth_year:{};tel:{};status:{}\n'
        .format(id, f_name, s_name, patr_name, birth_year, tel, status))
    return

add_line()