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
