# глобальные переменные
userChoice = 0      # переменная, которая хранит выбор пользователя
ValuesOsemka = [78 , 94 , 69 , 96 , 11 , 55 , 44 , 32 , 64 , 12 , 15 , 92 , 1 , 2 , 3]         # Задание 1: объявить переменную, котоая будет хранить 15 значений


# Выводим меню пользователя
print('Меню:')
print('1. Вывести на экран все значения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('6. Выйти')
print('Введите опцию:')

# Считываем ввод пользователя с клавиатуры



# Задание 2: в цикле while создать ограничения для ввода опций таким образом, чтобы
# программа принимала только знаенчия, из меню (1-6), в остальных случаях выдвала ошибку.
while userChoice != 6:
        userChoice = int(input())
        if userChoice == 1:
            print(ValuesOsemka)
        # Задание 3: добавить новое значение.
        elif userChoice == 2:
            print('Введите новое число:')
            newValue = int(input())
            ValuesOsemka.append(newValue)
            print(ValuesOsemka)
        # Задание 4: реализовать удаление значений путем перезаписи идей справа на лево.
        elif userChoice == 3:
            if len(ValuesOsemka) != 0:
                print('Введите число для удаления:')
                searchValue = int(input())
                counter = 0
                deleted = False
                for count in range(0, len(ValuesOsemka)):
                    if (ValuesOsemka[count] == searchValue) & (count < len(ValuesOsemka)):
                        deleted = True
                        while count+1 < len(ValuesOsemka):
                            ValuesOsemka[count] = ValuesOsemka[count+1]
                            count = count+1
                if deleted is True:
                    del ValuesOsemka[count]
                    print(ValuesOsemka)
                elif deleted is False:
                    print('Значения нет в базе данных.')
            else:
                print('База пустая! Добавте значения!')
        # Задание 4: реализовать поиск значения с выводом его индекса в списке.
        elif userChoice == 4:
            if len(ValuesOsemka) != 0:
                print('Введите число для поиска его индекса:')
                searchValue = int(input())
                found = False
                for count in range(0, len(ValuesOsemka)):
                    if ValuesOsemka[count] == searchValue:
                        found = True
                        print('Индекс значения "', searchValue, '":', count)
                if found is False:
                    print('Значение не найдено!')
            else:
                print('База пустая! Не можем искать!')
        elif userChoice == 5 :
            def bubble_sort(ValuesOsemka):
                for num in range(len(ValuesOsemka) - 1, 0, -1):
                    for item in range(num):
                        if ValuesOsemka[item] > ValuesOsemka[item + 1]:
                            ValuesOsemka[item], ValuesOsemka[item + 1] = ValuesOsemka[item + 1], ValuesOsemka[item]
                return ValuesOsemka

            print("Исхожный массив: ", ValuesOsemka)
            result = bubble_sort(ValuesOsemka)
            print("Результат сортировки:", result)
        else:
            print('Ошибка. Выберите существующую опцию')

        print('Меню:')
        print('1. Вывести на экран все значения')
        print('2. Добавить значение')
        print('3. Удалить значение')
        print('4. Найти значение')
        print('5. Отсортировать значения')
        print('Введите опцию:')