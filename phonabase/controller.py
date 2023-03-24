import data_base as db
from parameters import name_file_db

def init_db():
    return db.read_element(name_file_db)

# получение записи строки в виде списка без печати
def get_element_list(position_in_list: int) -> list:
    list_phone = init_db()
    return list_phone[position_in_list].split(' ' + ';' + ' ')

# список печатаем красиво
def view_list(list_phone: list) -> str:
    data = ''
    for i in range(len(list_phone)):
        if i < len(list_phone) - 1:
            data += str(list_phone[i]) + ' | '
        else:
            data += str(list_phone[i]) + ' | ' + '\n'
    #[print(list_phone[i], ' | ', end=' ') if i < len(list_phone) - 1 else print(list_phone[i], ' | ', '\n') for i in range(len(list_phone)) ]
    return data

# # заглавия колонок
def column_header():
    print(view_list(['Фамилия','Имя','Телефон','Пометка']))
        
# смотрим всю базу
def view_all_list():
    list_phone = init_db()
    column_header()              # через заглавия колонок
    [print(view_list(get_element_list(i))) for i in range(len(list_phone))]    
    

# добавляем и меняем записи
def add_record_in_list_universal() -> str:
    return str(input('Введите фамилию: ')) + ' ; ' + str(input('Введите имя: ')) + ' ; ' + str(input('Введите телефон: ')) + ' ; ' + str(input('Пометка: ')) + '\n'

# добавляем
def add_record_in_list():
    data = add_record_in_list_universal()
    db.write_element('a', data, name_file_db)
    print('Запись добавлена!')    

# ищем по ключевому
def enter_key_word() -> str:
    return str(input('Введите слово для поиска: '))

# удаляем по ключевому
def delete_record_in_list() -> db.write_element:
    list_phone = init_db()
    key_word = enter_key_word()
    result = ''
    for i in range(len(list_phone)):
        entry = get_element_list(i)
        for j in entry:
            find_word = False
            if key_word in j:
                find_word = True
                column_header()
                print(view_list(['Фамилия','Имя','Телефон','Пометка']))
                print(view_list(entry))
                for_delete = 'Да'
                for_delete = str(input('Хотите удалить запись? (Да/Нет):'))
                if for_delete == 'Да' or for_delete == "":
                    print("Запись удалена!")                    
                    break
        if find_word == False:
            result += " ; ".join(entry) + '\n'
    db.write_element('w', result, name_file_db)

# ищем запись в базе
def find_record_in_list():
    list_phone = init_db()
    key_word = enter_key_word()
    result = ''
    for i in range(len(list_phone)):
        entry = get_element_list(i)
        for j in entry:
            find_word = False
            if key_word in j:
                find_word = True
                # column_header()
                print(view_list(['Фамилия','Имя','Телефон','Пометка']))
                print(view_list(entry))
                #break

# редактируем запись по ключевому
def editing_record_in_list() -> db.write_element:
    list_phone = init_db()
    key_word = enter_key_word()
    result = ''
    for i in range(len(list_phone)):
        entry = get_element_list(i)
        for j in entry:
            find_word = False
            if key_word in j:
                find_word = True
                # column_header()
                print(view_list(['Фамилия','Имя','Телефон','Пометка']))
                print(view_list(entry))
                for_delete = 'Да'
                for_delete = str(input('Хотите отредактировать? (Да/нет):'))
                if for_delete == 'Да' or for_delete == "":
                    result += add_record_in_list_universal()
                    print("Запись отредактирована!")                    
                    break
        if find_word == False:
            result += " ; ".join(entry) + '\n'
    db.write_element('w', result, name_file_db)