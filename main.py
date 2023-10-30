import re


def selective_menu():
    print(
        '1. Распечатать справочник',
        '2. Найти телефон',
        '3. Изменить номер телефона',
        '4. Удалить запись',
        '5. Найти абонента по номеру телефона',
        '5. Добавить абонента в справочник',
        '7. Закончить работу', sep='\n'
    )
    choice = input("введите номер запроса:   ")
    return choice

#          ------ работа в справочнике ------

def Queries_in_the_directory():

    choice = selective_menu()
    #          ------ функции справочника ------

    # распечатать справочник
    def Print_the_guide():
        with open('phon.txt', 'r', encoding='utf-8') as data_numbers:
            print(data_numbers.read())
            print()

    # найти телефон
    def Find_phone():
        with open('phon.txt', 'r') as file:
            data = file.readlines()

        find = input("Введите Фамилию или Имя:   ").lower()

        print(f" Результаты поиска по запросу: {find}")
        for row in data:
            line = list(row.split(","))

            if find == "":
                print(f"По запросу {find} ничего не найдено.")
                break
            elif find in line[0].lower() or find in line[1].lower():  # or line[1].lower():
                print(f"{line[0]} {line[1]} - {int(line[2])}")
                break
        else:
            print(f"По запросу {find} ничего не найдено.")
        print()

        print(
            '1. Найти телефон',
            'Enter. Выход в главное меню',
            sep='\n'
        )
        req = input("Введите номер запроса:   ")

        match req:
            case '1':
                Find_phone()

    # изменить номер телефона
    def Change_phone_number():

        with open('phon.txt', 'r') as file:
            data = file.readlines()

        print("Смена номера:")
        find = input("Введите Фамилию или Имя абонента:   ").lower()

        print(f" Результаты поиска по запросу: {find}")
        for row in data:
            line = list(row.split(","))

            if find == "":
                print(f"По запросу {find} ничего не найдено.")
                break
            elif find in line[0].lower() or find in line[1].lower():
                print(f"{line[0]} {line[1]} - {int(line[2])}")

                with open('phon.txt', 'r') as f:
                    old_data = f.read()

                new_number = input(f"Введите новый номер абонента {line[0]} {line[1]}")

                if new_number == "":
                    print("Неккоректно веден номер")
                    Change_phone_number()
                else:
                    new_data = old_data.replace(line[2], new_number)

                    with open('phon.txt', 'w') as f:
                        f.write(new_data)
                    print(f"Номер успешно изменен на {new_number}")
                    break
        else:
            print(f"По запросу {find} ничего не найдено.")
        print()

        print(
            '1. Найти телефон',
            'Enter. Выход в главное меню',
            sep='\n'
        )
        req = input("Введите номер запроса:   ")

        match req:
            case '1':
                Change_phone_number()

    # удалить запись
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

    # найти абонента по номеру телефона
    def Find_a_subscriber_by_phone_number():
        return

    # добавить абонента в справочник
    def Add_a_subscriber_to_the_directory():
        return

    while (choice != 7):

        match choice:
            case '1':
                Print_the_guide()
            case '2':
                Find_phone()
            case '3':
                Change_phone_number()

        choice = selective_menu()



Queries_in_the_directory()