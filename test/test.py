
def Find_a_subscriber_by_phone_number():

    with open('test_phone.txt', 'r') as file:
        data = file.readlines()

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
            count-=1
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


Find_a_subscriber_by_phone_number()