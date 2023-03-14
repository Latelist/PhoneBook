from view import *
from database import *
lst = [1,2,3,4,5,6]

def control():
    while True:
        req = request()
        if req == 1:
            contact = save_data()
            write_data(contact)
        elif req == 2:
            string = output()
            print(read_data(string))
        elif req == 3:
            string = output()
            contacts = change_data(string)
            new_data(contacts)
        elif req == 4:
            p = parameter()
            sort(p)
        elif req == 5:
            print_data()
        elif req == 6:
            break
        else:
            req = int(input('Повторите ввод: '))


        



