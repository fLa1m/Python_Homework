def menu() -> int:
    commands = ["Показать все контакты", "Найти контакт", "Создать контакт"]
    print("Укажите номер команды: ")
    print("\n".join(f"{n}. {v}" for n, v in enumerate(commands, 1)))
    choice = input(">>> ")
    a = choice

    try:
        choice = int(choice)
        if choice < 0 or len(commands) < choice:
            raise Exception("Такой команды нет.")
    except ValueError:
        print("Повторите ввод.")
        return menu()
    except Exception:
        print("Такой команды нет.")
        return menu()
    else:
        return choice


var = menu()

print(type(var))
print(var)
