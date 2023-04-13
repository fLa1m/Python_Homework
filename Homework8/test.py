commands = ["Показать все контакты", "Найти контакт", "Создать контакт"]


def select_menu(commands: list) -> int:
    select = input(">>> ")

    try:
        select = int(select)
        if select < 0 or len(commands) < select:
            raise Exception("Такой команды нет.")
    except ValueError as ex:
        print("Повторите ввод.")
        select_menu(commands)
    except Exception as ex:
        print(ex)
        select_menu(commands)
    else:
        return int(select)


print(type(select_menu(commands)))
