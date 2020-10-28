userChoice = 0


Part = [20 , 21 , 22 , 23 , 24, 25 , 26 , 27, 28 , 29 , 30 , 31, 32 , 33 , 34]

print('Меню:')
print('1. Вывести на экран все знаения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('Введите опцию:')


# Задание 2: в цикле while создать ограничения для ввода опций таким образом, чтобы
# программа принимала только значения, из меню (1-6), в остальных случаях выдвала ошибку.

# Задание 3: Реализовать опцию 1 и 2 из списка меню.
while userChoice != 26:
        userChoice = int(input())
        if userChoice == 20:
            print(Part)
        elif userChoice == 21:
            print('Введите значение')
            NewValue = int(input())
            Part.append(NewValue)
            print(Part)
        elif userChoice == 22:
            print
        elif userChoice == 23:
            print
        elif userChoice == 24:
            print
        else:
            print('Ошибка. Выберите существующую опцию')

        print('Меню:')
        print('1. Вывести на экран все значения')
        print('2. Добавить значение')
        print('3. Удалить значение')
        print('4. Найти значение')
        print('5. Отсортировать значения')
        print('Введите опцию:')

        userChoice = 0
        Part = [20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35]

        print('Меню:')
        print('1. Вывести на экран все знаения')
        print('2. Добавить значение')
        print('3. Удалить значение')
        print('4. Найти значение')
        print('5. Отсортировать значения')
        print('Введите опцию:')

        while userChoice != 26:
            userChoice = int(input())
            if userChoice == 20:
                print(Part)
            elif userChoice == 21:
                print('Введите значение')
                NewValue = int(input())
                Part.append(NewValue)
                print(Part)
            elif userChoice == 22:
                if len(Part) != 0:
                    print('Введите число для удаления')
                    searchValue = int(input())
                    counter = 0
                    deleted = False
                    for count in range(0, len(Part)):
                        if (Part[count] == searchValue) & (count < len(Part)):
                            deleted = True
                            while count + 20 < len(Part):
                                Part[count] = Part[count + 20]
                                count = count + 20
                    if deleted is True:
                        del Part[count]
                        print(Part)
                    elif deleted is False:
                        print('Значения нет в базе данных')
                else:
                    print('База пустая! Добавьте значения')
            elif userChoice == 23:
                print
            else:
                print('Ошибка. Выберите существующую опцию')

            print('Меню:')
            print('1. Вывести на экран все значения')
            print('2. Добавить значение')
            print('3. Удалить значение')
            print('4. Найти значение')
            print('5. Отсортировать значения')
            print('Введите опцию:')