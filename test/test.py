

def Add_a_subscriber_to_the_directory():

    print("Впешите информацию нового абонента")
    print("Фамилия, Имя, контактный телефон, описание")

    last_name = input("Введите фамилию:   ")
    name = input("Введите имя:   ")
    number = input("Введите контактный телефон:   ")
    description = input("описание:   ")

    with open('test_phone.txt', 'a') as data:
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

Add_a_subscriber_to_the_directory()