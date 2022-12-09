#
# Модифицируйте класс Группа (задание прошлой лекции) так, чтобы при попытке добавления в группу более 10-ти студентов, было возбужденно пользовательское исключение.
# Таким образом
# нужно создать еще и пользовательское исключение для этой ситуации. И обработать его.

class GroupSizeException(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

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
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise GroupSizeException('в группе может быть максимум 10 студентов')


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
st3 = Student('Male', 20, 'Alex', 'Black', 'AN142')
st4 = Student('Female', 19, 'Bob', 'Bell', 'AN145')
st5 = Student('Male', 24, 'Dave', 'Jons', 'AN142')
st6 = Student('Female', 26, 'Kira', 'Brown', 'AN145')
st7 = Student('Male', 30, 'Josh', 'White', 'AN142')
st8 = Student('Female', 29, 'Margo', 'Kim', 'AN145')
st9 = Student('Male', 24, 'Abraham', 'Robbie', 'AN142')
st10 = Student('Female', 28, 'Valencio', 'Mucho', 'AN145')
st11 = Student('Female', 33, 'Roberto', 'Rodrigo', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(gr)

try:
    gr.add_student(st11)
except GroupSizeException as error:
    print(error)
