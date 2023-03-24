from sys import exit
import controller

def ui():
    print("\n")
    print("Функции справочника:")
    print("1 - Просмотр всего справочника")
    print("2 - Поиск записи")
    print("3 - Добавление данных")
    print("4 - Редактирование данных")
    print("5 - Удаление данных")
    print("6 - Выход из справочника")
    print("\n")

    choice = int(input("Что Вы хотите сделать? Введите цифру: "))
    print("\n")

    match choice:
        case 1:
            controller.view_all_list()
            ui()
        case 2:
            controller.find_record_in_list()
            ui()
        case 3:
            controller.add_record_in_list()
            ui()
        case 4:
            controller.editing_record_in_list()
            ui()
        case 5:
            controller.delete_record_in_list()
            ui()
        case 6:
            exit()
        case _:
            ui()