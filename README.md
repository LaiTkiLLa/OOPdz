
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courser = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_student = f"Имя: {self.name} Фамилия: {self.surname}"
        return some_student

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def avarage(self):
        for keys, values in self.grades.items():
            return sum(values)/len(values)



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self, ):
        some_lecturer = f"Имя: {self.name} Фамилия: {self.surname}"
        return some_lecturer

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Deduction']

cool_lecturer = Lecturer('Sherlock', 'Holmes')
cool_lecturer.courses_attached += ['Deduction']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 4)

best_student.rate_lecture(cool_lecturer, 'Deduction', 10)
best_student.rate_lecture(cool_lecturer, 'Deduction', 5)
best_student.rate_lecture(cool_lecturer, 'Deduction', 3)

print(cool_lecturer.grades)

print(best_student.grades)

some_lecturer = Reviewer('Some', 'Reviewer')
print(some_lecturer)

print(cool_lecturer.avarage())



