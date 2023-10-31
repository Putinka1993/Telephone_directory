import re
from utils import read_file
def selective_menu():
    print(
        '1. Распечатать справочник',
        '2. Найти телефон',
        '3. Изменить номер телефона',
        '4. Удалить запись',
        '5. Найти абонента по номеру телефона',
        '6. Добавить абонента в справочник',
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

        data = read_file('phon.txt')

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

        data = read_file('phon.txt')

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

        with open('phon.txt') as f:
            lines = f.readlines()

        delete_contact = input("Выберете контакт который хотите удалить:   ").lower()
        pattern = re.compile(re.escape(delete_contact))

        with open('phon.txt', 'w') as f:
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

        data = read_file('phon.txt')

        find_number = input("Введите номер абонента:   ")

        print(f" Результаты поиска по запросу: {find_number}")
        count = 0
        for row in data:
            line = list(row.split(","))
            count += 1
            if not find_number.isdigit():
                print("Введены неправильные символы, попробуйте еще раз.")
                Find_a_subscriber_by_phone_number()

            elif int(find_number) == int("".join(list(filter(lambda x: x.isdigit(), line[2])))):
                print(f"{line[0]} {line[1]} - {int(line[2])}")
                count -= 1
                continue

        if count == len(data):
            print(f"По запросу {find_number} ничего не найдено.")
        print()

        print(
            '1. Найти телефон',
            'Enter. Выход в главное меню',
            sep='\n'
        )
        req = input("Введите номер запроса:   ")

        match req:
            case '1':
                Find_a_subscriber_by_phone_number()

    # добавить абонента в справочник
    def Add_a_subscriber_to_the_directory():

        print("Впешите информацию нового абонента")
        print("Фамилия, Имя, контактный телефон, описание")

        last_name = input("Введите фамилию:   ")
        name = input("Введите имя:   ")
        number = input("Введите контактный телефон:   ")
        description = input("описание:   ")

        with open('phon.txt', 'a') as data:
            data.write(f'{last_name}, {name}, {number}, {description}.\n')

        print(
            '1. Вписать нового абонента',
            'Enter. Выход в главное меню',
            sep='\n'
        )
        req = input("Введите номер запроса:   ")

        match req:
            case '1':
                Add_a_subscriber_to_the_directory()

    while (choice != '7'):

        match choice:
            case '1':
                Print_the_guide()
            case '2':
                Find_phone()
            case '3':
                Change_phone_number()
            case '4':
                Delete_entry()
            case '5':
                Find_a_subscriber_by_phone_number()
            case '6':
                Add_a_subscriber_to_the_directory()


        choice = selective_menu()



Queries_in_the_directory()