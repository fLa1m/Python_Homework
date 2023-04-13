# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import json
import os


def path_file(file_name="phone_book"):
    return os.path.join(os.path.dirname(__file__), f"{file_name}.txt")


def save_file(contacts: list):
    path = path_file()

    with open(path, "w", encoding="UTF-8") as file:
        json.dump(contacts, file, ensure_ascii=False)


def load_from_file():
    path = path_file()

    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)

    return data


def screen(contacts):
    keys = dict(
        first_name="Имя",
        second_name="Фамилия",
        middle_name="Отчество",
        phone_number="Телефон",
    )

    text = str()
    title = str()

    for num, el in enumerate(contacts, 1):
        title += "№".ljust(3) + " ".join(f"{keys[k]}".ljust(15) for k in el.keys())
        title += (
            "\n-------------------------------------------------------------------\n"
        )
        break

    for num, el in enumerate(contacts, 1):
        text += f"{num}.".ljust(3) + " ".join(f"{v}".ljust(15) for v in el.values())
        text += (
            "\n-------------------------------------------------------------------\n"
        )

    print(title, text, sep="")


def new_contact():
    contact = dict(
        second_name=input("Введите фамилию: "),
        first_name=input("Введите имя: "),
        middle_name=input("Введите отчество: "),
        phone_number=input("Введите номер телефона: "),
    )
    return contact


def add_contact(contacts: list):
    contacts.append(new_contact())


def support_find(book: dict, find):
    for v in book.values():
        if find.lower() in v.lower():
            return book


def screen_find_contact(contacts):
    val = find_contact(contacts)
    if val:
        screen(val)
    else:
        print("Нет контактов.")


def find_contact(contacts):
    print("Введите данные для поиска.")
    value = input(">>> ")
    result = list(filter(lambda x: support_find(x, value), contacts))
    return result


def change_contact(contacts):
    keys = dict(
        first_name="Имя",
        second_name="Фамилия",
        middle_name="Отчество",
        phone_number="Телефон",
    )

    val: list = find_contact(contacts)

    if val:
        screen(val)

        print("Укажите номер контакта для изменения.")
        contact = list()
        select_contact = select_menu(val) - 1
        contact.append(val[select_contact])
        contact_keys = list(val[select_contact])

        print("Укажите номер изменяемого поля.")
        contact_list = str()
        for num, el in enumerate(contact_keys, 1):
            contact_list += "".join(f"{num}. {keys[el]}") + "\n"
        print(contact_list)

        select = select_menu(contact_keys)
        dict_val = val[select_contact]

        print("Введите новое значение.")
        dict_val[contact_keys[select - 1]] = input(
            f"{keys[contact_keys[select - 1]]}:\n>>> "
        )

    else:
        print("Нет контактов.")
        change_contact(contacts)


def menu():
    commands = [
        "Показать все контакты",
        "Добавить контакт",
        "Поиск контакта",
        "Изменить контакт",
    ]
    print("Укажите номер команды: ")
    print("\n".join(f"{k}. {v}" for k, v in enumerate(commands, 1)))
    return select_menu(commands)


def select_menu(commands: list) -> int:
    select = input(">>> ")

    try:
        select = int(select)
        if select < 0 or len(commands) < select:
            raise Exception("Такой команды нет.")
    except ValueError as ex:
        print("Повторите ввод.")
        return select_menu(commands)
    except Exception as ex:
        print(ex)
        return select_menu(commands)
    else:
        return select


def main():
    data = load_from_file()

    command = menu()
    if command == 1:
        screen(data)
    elif command == 2:
        add_contact(data)
    elif command == 3:
        screen_find_contact(data)
    elif command == 4:
        change_contact(data)

    save_file(data)


if __name__ == "__main__":
    main()
