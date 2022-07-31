def del_data(data_for_del: str):
    with open('fio.csv', 'r', encoding="utf-8") as data:
        lines = data.readlines()
        # print(*lines) - для визуальной проверки
    with open('fio.csv', 'w', encoding="utf-8") as data:
        for line in lines:
            if data_for_del not in line:
                data.write(line)
    # print(*lines) - для визуальной проверки

