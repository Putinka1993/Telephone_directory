import re


def Delete_entry():


    with open('test_phone.txt') as f:
        lines = f.readlines()

    delete_contact = input("Выберете контакт который хотите удалить:   ").lower()
    pattern = re.compile(re.escape(delete_contact))

    with open('test_phone.txt', 'w') as f:
        count = 0
        for line in lines:
            result = pattern.search(line.lower())
            if result is None:
                f.write(line)
                count += 1

        if count == len(lines):
            print(f"Результатов по запросу {delete_contact} нету в записной книжке")

        print(
            '1. Найти телефон',
            'Enter. Выход в главное меню',
            sep='\n'
        )
        req = input("Введите номер запроса:   ")

        match req:
            case '1':
                Delete_entry()


Delete_entry()