userChoice = 0
ValuesOsemka = [78 , 94 , 69 , 96 , 11 , 55 , 44 , 32 , 64 , 12 , 15 , 92 , 1 , 2 , 3]

print('Меню:')
print('1. Вывести на экран все значения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('Введите опцию:')

while userChoice != 6:
        userChoice = int(input())
        if userChoice == 1:
            print(ValuesOsemka)
        elif userChoice == 2:
            print('Введите значение')
            NewValue = int(input())
            ValuesOsemka.append(NewValue)
            print(ValuesOsemka)
        elif userChoice == 3:
            if len(ValuesOsemka) !=0 :
                print('Введите число для удаления')
                searchValue = int(input())
                counter = 0
                deleted = False
                for count in range(0,len(ValuesOsemka)) :
                    if (ValuesOsemka[count] == searchValue) & (count < len(ValuesOsemka)):
                        deleted = True
                        while count+1 < len(ValuesOsemka):
                            ValuesOsemka[count] = ValuesOsemka[count+1]
                            count = count+1
                if deleted is True :
                    del ValuesOsemka[count]
                    print(ValuesOsemka)
                elif deleted is False :
                    print('Значения нет в базе данных')
            else:
                print('База пустая! Добавьте значения')
        elif userChoice == 4:
            try:
                print('Введите число для поиска его индекса:')
                index = ValuesOsemka.index(int(input()))
                print('Индекс этого числа равен')
                print(index)
            except ValueError:
                print("значение не найдено")
        elif userChoice == 5:
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