
# 1. Циклы
# Проверочный ввод данных, цикл While и For

def sep ():
    Separator = input("Введите символ: ")
    Znachenie_Separatora = 100

    povtorim = 1
    while (povtorim == 1):
        #Расчет квадрата
        print(Separator * Znachenie_Separatora) #Распеатываем разделитель
        kv = 1
        while (kv==1):
            try:
                kvadrat = float(input("\n1.КВАДРАТ.\n Введите длинну стороны (в сантиметрах): "))
                if  kvadrat > 0:
                    print("_" * 36)
                    print("   Результат:                        ")
                    Perimetr_kv = kvadrat * 4
                    print("   Периметр квадрата равен:", Perimetr_kv, "см")
                    print("   Площадь квадрата равна:", kvadrat * kvadrat, "кв.см")
                    print("_" * 36)

                else:
                    print("\n!!Введено некорректное значение длинны квадрата, повторите попытку и введите значение >0")


            except ValueError:
                print("\n!!введено некорректное значение, введите пожалуйста значение >0")

            Povtor_1 = input("\n ---> Хотите повторить расчет квадрата? или перейдем к рассчету прямоугольника? (нажмите 'K' (англ.) - квадрат / нажмите 'P' (англ.) - прямоугольник) ")

            if Povtor_1 == "K":
                kv = 1
            elif Povtor_1 == "k":
                kv = 1
            else:
                kv = 0
    return ()


# 2. Списки (без повторов)
def cook ():
    cook_book = [
                    ['1.Салат', [
                                    ['картофель', 100, 'гр.'],
                                    ['морковь', 50, 'гр.'],
                                    ['огурцы', 50, 'гр.'],
                                    ['горошек', 30, 'гр.'],
                                    ['майонез', 70, 'мл.'],
                                ]
                    ],

                    ['2.Пицца', [
                                    ['сыр', 50, 'гр.'],
                                    ['томаты', 50, 'гр.'],
                                    ['тесто', 100, 'гр.'],
                                    ['бекон', 30, 'гр.'],
                                    ['колбаса', 30, 'гр.'],
                                    ['грибы', 20, 'гр.'],
                                 ],
                    ],

                    [ '3.Фруктовый десерт', [
                                                ['хурма', 60, 'гр.'],
                                                ['киви', 60, 'гр.'],
                                                ['творог', 60, 'гр.'],
                                                ['сахар', 10, 'гр.'],
                                                ['мед', 50, 'мл.'],
                                             ]
                    ]
                ]



    try:
        count_person = int(input("\nВведите количество персон, для которых готовить ужин:"))
    except:
        print("\nВы ввели неверное значение!")

    #3. Считаем длину всей книги (cook_book)
    lenght_cookbook = len(cook_book)
    print(f'длинна всей книги - {lenght_cookbook}')

    #4. Вывод общей строки
    print(f'\nРецепт {lenght_cookbook} блюд для приготовления на {count_person} персон:')

    #5. Счетчики
    count_k = 0
    i = 0
    number = 0

    #6. Вывод
    while (number < lenght_cookbook):
        print(f'\n{cook_book[count_k][0]}:')
        for result in cook_book[count_k][1]:
            cook_iter = cook_book[count_k][1][i][1]
            cook_result = cook_iter * count_person

            print(f'{cook_book[count_k][1][i][0]}: {cook_result} гр.')
            i += 1

        count_k += 1
        i = 0
        number += 1
    return


# 3. Словари.
def geo ():
    geo_logs = [
                    {'visit1': ['Москва', 'Россия']},
                    {'visit2': ['Дели', 'Индия']},
                    {'visit3': ['Владимир', 'Россия']},
                    {'visit4': ['Лиссабон', 'Португалия']},
                    {'visit5': ['Париж', 'Франция']},
                    {'visit6': ['Лиссабон', 'Португалия']},
                    {'visit7': ['Тула', 'Россия']},
                    {'visit8': ['Тула', 'Россия']},
                    {'visit9': ['Курск', 'Россия']},
                    {'visit10': ['Архангельск', 'Россия']}
               ]

    #1. Проходим по списку geo_logs
    #2. Переводим каждый элемент списка {visit: ['Город', 'Страна']} в dictionary и помещаем словарь в dict_all
    #3. Каждое значение (value) словаря с ключом visit{i} переводим в список ['город', 'Страна'] и заливаем в list_2
    #4. Проверяем второй элемент списка на совпадение "Россия", если совпало, то ничего не делаем, если не совпало, то заменяем элемент на "1"
    #5. В итоге получается список из элементов с Россией и единиц (1)
    #6. Затем пробегаемся по спику и удаляем элементы "1". Учитывая, что метод "remove" удаляет только первый совпавшийся элемент, мы пробегаемся заново по новому списку до тех пор пока все элементы не будут удалены

    a = geo_logs[0]
    print(a['visit1'])

    i=0
    for list_geo in geo_logs:
        dict_all = dict(geo_logs[i])
        list_2 = list(dict_all[f'visit{i+1}'])

        if (list_2[1] == 'Россия'):
            i=i+1
        else:
            geo_logs[i] = 1
            i=i+1

    lenght_geo = len(geo_logs)

    try:
        count = 0
        while (count < lenght_geo):
            geo_logs.remove(1)
            count += 1

    except:
        print ("Список визитов по городам России:\n")
        for result in geo_logs:
            print(result)
    return



# 4. Множества
def idss ():
    ids = {
            'user1': [213, 213, 213, 15, 213],
            'user2': [54, 54, 119, 119, 119],
            'user3': [213, 98, 98, 35],
            'user4': [1000, 98, 119, 213]   #ПРОВЕРКА
           }

    i=1
    spisok_all = []
    while (i <= len(ids)):
        spisok_all += ids[f'user{i}']
        i += 1

    ids_set = set(spisok_all)
    ids_list = list(ids_set)
    print(f'Список уникальных id:\n{ids_list}')

    return



# 5. Функции
documents = [
                {"type": "passport", "number": "2207 876234", "name": "Василий Губкин"},
                {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
            ]

#Перечень полок, на которых находятся документы:

directories = {
                '1': ['2207 876234', '11-2', '5455 028765'],
                '2': ['10006'],
                '3': []
              }



#1.Функция p-people. Выдает имя человека, которому принадлежит номер документа
def number_name():
    number_vvod = input("\nВведите номер документа: ")

    for result_name in documents:
        if (number_vvod == result_name['number']):
            print(result_name['name'])
            return

    print("Имени человека с данным номером документа в базе нет")


#2.Функция s-shelf. Команда, которая спросит номер документа и выведет номер полки, на которой он находится
def number_directories():
    number_vvod = input("\nВведите номер документа: ")


    for result_direct in documents:
        if (result_direct['number'] == number_vvod):
            number_dir = 1
            count_list = 0

            for result_all in directories:
                list_direct = directories[f'{number_dir}']

                while (count_list < len(list_direct)):
                    if (list_direct[count_list] == number_vvod):
                        print(f"Номер полки, на которой находится документ: {number_dir}")
                        count_list += 1

                    else:
                        count_list += 1

                number_dir += 1
                count_list = 0

            return


    print("Документ с данным номером на полках отсутствует")


#3.Функция l-list. Выдает список всех документовв формате: passport "2207 876234" "Василий Губкин"

def all_list():
    print("\nВесь список документов:")
    for result_doc in documents:
        print(result_doc['type'] + ' "' + result_doc['number'] + '" ' ' "' + result_doc['name'] + '"')


#4. Функция a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
def add_doc():
    numb_dir = int(input("\nВведите номер полки, на которую необходимо добавить документ:"))
    l_d = len(directories)
    if (numb_dir > l_d):
        print(f"Будьте внимательны, такая полка отсутствует. На текущий момент кол-во полок: {l_d}")
        return

    else:
        print("Начинаем добавление документы в каталог и на полку ->")
        a = input("\nВведите тип документа (passport / invoice / insurance):")
        b = input("Введите номер документа:")
        c = input("Введите имя владельца документом:")

        new_d = {"type": f'{a}', "number": f'{b}', "name": f'{c}'}
        documents.append(new_d)
        directories[f'{numb_dir}'].append(b)
        print("Добавление документа прошло успешно!")




#Main - функция

def main():
    while True:
        inp_function = input("\nВведите название функции (\np  \ns  \nl  \na \nsep - функция разделения  \ncook - кулинарная книга \nid - уникальные значения\nиное значение - выход из программы) : ").lower()

        if (inp_function == 'p'):
            number_name()

        elif (inp_function == 's'):
            number_directories()

        elif (inp_function == 'l'):
            all_list()

        elif (inp_function == 'a'):
            add_doc()

        elif (inp_function == 'sep'):
            sep()
            
        elif (inp_function == 'cook'):
            cook()

        elif (inp_function == 'id'):
            idss()


        else:
            print("Good bye")
            break


main()














