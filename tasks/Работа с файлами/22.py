def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес: ')

def create_contact():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()

    return f'{name} {surname} {patronymic} {phone} {address}'

def add_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)

   

def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        print(file.read().rstrip())

def search_contact():
    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = contact_str.split()
        if any(search.lower() in field.lower() for field in contact_lst):
            print(contact_str)

def import_contacts():
    filename = input('Введите имя файла для импорта: ')
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            data = file.read()
            with open('phonebook.txt', 'a', encoding='UTF-8') as phonebook_file:
                phonebook_file.write(data)
        print(f'Данные из файла {filename} успешно импортированы.')
    except FileNotFoundError:
        print(f'Файл {filename} не найден.')

def export_contacts():
    filename = input('Введите имя файла для экспорта: ')
    with open('phonebook.txt', 'r', encoding='UTF-8') as phonebook_file:
        data = phonebook_file.read()
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(data)
    print(f'Данные успешно экспортированы в файл {filename}.')

def copy_contact():
    try:
        source_filename = input('Введите имя файла, откуда скопировать контакт: ')
        line_number = int(input('Введите номер строки для копирования: '))

        with open(source_filename, 'r', encoding='UTF-8') as source_file:
            lines = source_file.readlines()

            if 1 <= line_number <= len(lines):
                contact_to_copy = ''.join(lines[line_number - 1:line_number + 1])

                target_filename = input('Введите имя файла, куда скопировать контакт: ')

                with open(target_filename, 'a', encoding='UTF-8') as target_file:
                    target_file.write(contact_to_copy)
                
                print(f'Контакт успешно скопирован из строки {line_number} файла {source_filename} в файл {target_filename}.')
            else:
                print(f'Ошибка: Некорректный номер строки {line_number}.')

    except ValueError:
        print('Ошибка: Введите корректный номер строки (целое число).')
    except FileNotFoundError:
        print('Ошибка: Файл не найден.')


def interface():
    command = '-1'
    while command != '7':
        print("\nВсе возможные варианты:\n"
              "1. Добавить контакты\n"
              "2. Вывести на экран\n"
              "3. Поиск контакта\n"
              "4. Импорт/экспорт данных\n"
              "5. Копировать контакт из одного файла в другой\n"
              "6. Выход из программы")

        command = input("Введите номер действия: ")

        while command not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Некорректный ввод данных, нужно ввести число команды')
            command = input("Введите номер действия: ")

        match command:
            case '1':
                add_contact()
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                print("\n1. Импорт данных\n"
                      "2. Экспорт данных")
                sub_command = input("Введите номер действия: ")
                match sub_command:
                    case '1':
                        import_contacts()
                    case '2':
                        export_contacts()
            case '5':
                copy_contact()
            case '6':
                print('Всего хорошего')

interface()
