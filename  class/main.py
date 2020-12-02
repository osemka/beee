class Student():
    def __init__ (self, name, gps, age, group):
        self.name = name
        self.age = age
        self.gps = gps
        self.group = group


    def StudentData(self):
        return 'ФИО: ' + self.name, 'Возраст: ' + self.age, 'Город: ' + self.gps, 'Группа: ' + self.group

student1 = Student('Серикова Асем', '18', 'Атырау', 'Аиу-19 р/о')
student2 = Student('Болатов Парвиз', '18', 'Атырау', 'Аиу-19 р/о')
student3 = Student('Сабырова Индира', '18', 'Атырау', 'Аиу-19 р/о')
student4 = Student('Амангельдиева Гульмира', '18', 'Атырау', 'Аиу-19 р/о')
student5 = Student('Каймуллдиев Данияр', '18', 'Атырау', 'Аиу-19 р/о')


print(*(student1.StudentData()), sep='\n')
print('*****************************************')
print(*(student2.StudentData()), sep='\n')
print('*****************************************')
print(*(student3.StudentData()), sep='\n')
print('*****************************************')
print(*(student4.StudentData()), sep='\n')
print('*****************************************')
print(*(student5.StudentData()), sep='\n')
