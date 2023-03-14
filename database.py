def write_data(contact):
    with open('file.txt', 'a', encoding = 'utf-8') as data:
        for i in contact:
            data.write(f'{i} ')

def read_data(string):
    result = 0
    with open('file.txt', 'r') as data:
        contacts = data.readlines()
        for i in contacts:
            if string in i:
                result = i
    return result

def change_data(string):
    with open('file.txt', 'r+') as data:
        contacts = data.readlines()
        contacts = [i.strip() for i in contacts]
        for i in range(len(contacts)):
            if string in contacts[i]:
                print(contacts[i])
                print('Измените контакт')
                surname = input('Введите фамилию: ')
                name = input('Введите имя: ')
                number = input('Введите телефон: ')
                contacts[i] = f'{surname} {name} {number}'
    return contacts

def new_data(contacts):
    with open('file.txt', 'w') as data:
        for i in contacts:
            data.write(f'{i}\n')

def sort(p):
    with open('file.txt', 'r+') as data:
        contacts = data.readlines()
        contacts = [i.strip() for i in contacts]
        contacts = sorted(contacts, key = lambda x: x.split()[p])
        with open('file.txt', 'w') as data:
            for i in contacts:
                print(i)
                data.write(f'{i}\n')

def print_data():
    with open('file.txt', 'r') as data:
        contacts = data.readlines()
    for i in contacts:
        print(i)