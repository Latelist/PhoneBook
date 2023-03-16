def request():
    i = int(input('Введите 1, чтобы ввести данные.\n\
Введите 2, чтобы получить данные.\n\
Введите 3, чтобы изменить данные.\n\
Введите 4, чтобы отсортировать данные.\n\
Введите 5, чтобы вывести телефонную книгу.\n\
Введите 6, чтобы удалить контакт. \n\
Введите 7, чтобы выйти из программы.\n: '))
    return i

def save_data():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    number = input('Введите телефон: ')
    return (surname, name, number)

def output():
    r = input('Введите данные для поиска: ')
    return r

def print_data(data):
    print(data)

def parameter():
    p = int(input('Введите 0, чтобы отсортировать по фамилии.\n\
Введите 1, чтобы отсортировать по имени.\n\
Введите 2, чтобы отсортировать по номеру: '))
    return p


def print_data():
    with open('file.txt', 'r') as data:
        contacts = data.readlines()
    for i in contacts:
        print(i)