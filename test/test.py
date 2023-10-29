
def Change_phone_number():

    with open('test_phone.txt', 'r') as file:
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

            with open('test_phone.txt', 'r') as f:
                old_data = f.read()

            new_number = input(f"Введите новый номер абонента {line[0]} {line[1]}")

            if new_number == "":
                print("Неккоректно веден номер")
                Change_phone_number()
            else:
                new_data = old_data.replace(line[2], new_number)

                with open('test_phone.txt', 'w') as f:
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






Change_phone_number()