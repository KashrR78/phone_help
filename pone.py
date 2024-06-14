




def interface():
    print("Выберете необходимое действие : \n 1 - Отобразить весь справочник \n 2 - Найти абонента по фамилии \n 3 - Найти абанента по номеру телефона \n 4 - Добавить абанента в справочник \n 5 - Сохранить справочник в текстовом формате \n 6 - Копирования данных из одного файла в другой \n 7 - Завершение программы")
    command = int(input("Введите число "))
    while(True):
        match command:
            case 1:
                print_phone()
                break
            case 2:
                find_name()
                break
            case 3:
                find_fone()
                break
            case 4:
                creat_pone()
                break
            case 5:
                save_txt()
                break
            case 6:
                copu_txt()
                break
            case 7: break
            case _: print("Неправильное число")    
    print("Программа завершена")


def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, line.split(',')))
           phone_book.append(record)	
    return phone_book


def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}')

def print_phone():
    print('Вывожу данные справочника: \n')
    with open('phon.csv', 'r' , encoding='utf 8 ') as f:
        data_fers = f.read()
        print(data_fers)

def creat_pone():
        sername = input('Введите вашу фамилию: ')
        name = input('Введите ваше имя: ')
        phone = input('Введите ваш телефон: ')
        description =  input('Введите описание: ')
        with open('phon.csv', 'a' , encoding='utf 8 ') as f:
            f.write(f"{sername},{name},{phone},{description}")


def save_txt():
    nam = input('Введите имя файла: ')
    write_txt(f'{nam}.txt',phone_book)


def find_name():
    nam = input('Введите фалилию для поиска: ')
    temp = True
    for lis in phone_book:
        if nam == lis['Фамилия']:
            print(f'Абонент :{lis['Фамилия']} {lis['Имя']} тел: {lis['Телефон']} - {lis['Описание']}')
            temp = False
    if temp:
        print("Такой Фамили нет \n")

def find_fone():
    temp = True
    phon = input('Введите телефон для поиска: ')
    for lis in phone_book:
        if phon == lis['Телефон']:
            print(f'Абонент :{lis['Фамилия']} {lis['Имя']} тел: {lis['Телефон']} - {lis['Описание']}')
            temp = False
    if temp:
        print("Такого номера нет \n")

def copu_txt():
    num_lin = int(input("Какую строчку скопирывать в файл: "))
    while num_lin < 1 or num_lin > len(phone_book):
        print("Абанента с таким номером нет")
        print(f"В справочнике {int(len(phone_book))} абанента")
        num_lin = int(input("Какую строчку скопирывать в файл: "))
    nam = input('Введите имя файла: ')
    with open(f'{nam}.txt','w',encoding='utf-8') as copy:
            s=''
            for v in phone_book[num_lin-1].values():
                s = s + v + ','
            copy.write(f'{s[:-1]}')
      


phone_book=read_txt('phon.csv')
interface()




