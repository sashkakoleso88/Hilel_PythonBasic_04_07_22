#
# 1) Создайте класс, описывающий человека (создайте метод, выводящий информацию о человеке).
# 2) На его основе создайте класс Студент (переопределите метод вывода информации).
# 3) Создайте класс Группа, экземпляр которого, состоит из объектов класса Студент. Реализуйте методы добавления, удаления студента и метод поиска студента по фамилии.
# Метод поиска студента должен возвращать именно экземпляр класса Студент, если студент есть в группе, в противном случае - None.
# Определите для Группы метод __str__() для возвращения списка студентов в виде строки.


class Human:

    def __init__(self, gender, age, name, surname):
        self.gender = gender
        self.age = age
        self.name  = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname} {self.age}'


class Student(Human):

    def __init__(self, gender, age, name, surname, record_book):
        super().__init__(gender, age, name, surname)
        self.gender = gender
        self.age = age
        self.name = name
        self.surname = surname
        self.record_book = record_book

    def __str__(self):
        return f'Student {self.name} {self.surname}, record_book: {self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, surname):
        res = self.find_student(surname)
        if res:
            self.group.discard(res)

    def find_student(self, surname):
        res = None
        for student in self.group:
            if student.surname == surname:
                res = student
                break
        return res

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f'name: {student.name}, surname: {student.surname}, age: {student.age}\n'
        return f'Number:{self.number}\n{all_students} '



st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
gr.find_student('Jobs')
gr.find_student('Jobs2')  # None
print()
gr.delete_student('Taylor')
print(gr) # Only one student