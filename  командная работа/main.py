all_book = [[1, 'М.Булгаков','Мастер и Маргарита', "1937", 'выдано'],
            [2, 'М.Ю.Лермонтов', 'Герой нашего времени', '1876', 'в архиве']]
notes = [[1, 'Мастер и Маргарита', 'Кубашева Дильназ Бауыржановна', '15.11.2020'], [2]]
all_readers = [['Кубашева Дильназ Бауыржановна', '87776665544', 'pushkin street', 'kubasheva1310@gmail'],
               ['Серикова Асем Куанышевна', '87779993322', 'riverdale', 'tyui@gmail']]
debtor = [['Каймулдиев Данияр', 'Гарри Поттер и Философский камень'], ['Болатов Парвиз', 'Алхимик']]
userChoice = 0

print('Меню:')
print('1. Поиск читателя')
print('2. Поиск книги')
print('3. Добавить читателя')
print('4. Добавить книгу')
print('5. Выдать книгу')
print('6. Принять книгу')
print('7. Показать задолженности')
print('8. Выйти')
print('Введите опцию:')

userChoice = int(input())

while userChoice != 8:
    if (userChoice < 1) | (userChoice > 8):
        print('Такой опции нет, выберите существующую опцию.')
        userChoice = int(input())
    else:
        if userChoice == 1:
            def linear_search(sequince, element):
                for i in range(len(sequince)):
                    for j in range(len(sequince[i])):
                        if sequince[i][j] == element:
                            print(sequince[i])
                return 'founded'

            reader = str(input('Введите имя для поиска:'))
            print(linear_search(all_readers, reader))
            print(linear_search(notes, reader))

        elif userChoice == 2:
            def linear_search2(sequince, element):
                for i in range(len(sequince)):
                    for j in range(len(sequince[i])):
                        if sequince[i][j] == element:
                            print(sequince[i])
                return 'founded'
            book = str(input('Введите название книги для поиска:'))
            print(linear_search2(all_book, book))
            print(linear_search2(notes, book))
        elif userChoice == 3:
            def add(array):
                pass
        elif userChoice == 4:
            pass
        elif userChoice == 5:
            def give(array):
                id = int(input('Введите ID:'))
                for i in range(len(array)):
                    for j in range(len(array[i])):
                        if id == array[i][0]:
                            if array[i][4] == "в архиве":
                                array[i][4] = 'выдано'
                                print('Введите имя:')
                                reader = str(input())
                                notes[i].append(reader)
                                print('Введите дату выдачи:')
                                data = str(input())
                                notes[i].append(data)
                                print('Книга успешно выдана!')
                            else:
                                print('Извините, книга отсутствует в архиве')
                                break

                        else:
                            print('Введите верный ID')
                            break
                        #id = int(input())


                return array

            print(give(all_book))
            print(notes)

        elif userChoice == 6:
            def take(array):
                id = int(input('Введите ID:'))
                for i in range(len(array)):
                    for j in range(len(array[i])):
                        if id == array[i][0]:
                            if array[i][4] == "выдано":
                                array[i][4] = 'в архиве'
                                print('Введите дату дня получения:')
                                data = str(input())
                                notes[i].append(data)
                                print('Книга была получена!')
                            else:
                                print("Книга находится в архиве")
                                break
                        else:
                            print('Введите верный ID')
                            break
                        #id = int(input())

                return array

            print(take(all_book))
            print(notes)
        elif userChoice == 7:
            def debtors(array):
                return array
            print(debtors(debtor))

        print('\nМеню:')
        print('1. Поиск читателя')
        print('2. Поиск книги')
        print('3. Добавить читателя')
        print('4. Добавить книгу')
        print('5. Выдать книгу')
        print('6. Принять книгу')
        print('7. Показать задолженности')
        print('8. Выйти')
        print('Введите опцию:')
        userChoice = int(input())
