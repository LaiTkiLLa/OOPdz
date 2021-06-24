class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
          if course in lecturer.grades:
            lecturer.grades[course] += [grade]
          else:
            lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
      for values in self.grades.values():
        a = round(sum(values)/len(values), 2)
        return a

    def __lt__(self, best_student_2):
      if isinstance(best_student_2, Student) and self.average() < best_student_2.average():
        return
      else:
        return 'Такого студента нет'

    def __str__(self):
      a = f" Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние задания: {self.average()} \n Курсы в процессе обучения: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses}"
      return a
    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
  def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

  def average(self):
        for values in self.grades.values():
            a = round(sum(values)/len(values), 2)
            return a

  def __lt__(self, cool_lecturer_2):
    if isinstance(cool_lecturer_2, Lecturer) and self.average() < cool_lecturer_2.average():
      return
    else:
      return 'Такого лектора нет'

  def __str__(self):
    a = f" Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.average()}"
    return a


class Rewiewer(Mentor):

  def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

  def __str__(self):
    a = f" Имя: {self.name} \n Фамилия: {self.surname}"
    return a

best_student_1 = Student('Cannibal', 'Hannibal', 'm')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_1.courses_in_progress += ['Deduction', 'Surgery']
best_student_1.finished_courses += ['Введение в программирование']
best_student_2 = Student('Margaret', 'Thatcher', 'w')
best_student_2.courses_in_progress += ['Python', 'Git']
best_student_2.courses_in_progress += ['Deduction', 'Surgery']
best_student_2.finished_courses += ['Введение в программирование']

 
cool_reviewer = Rewiewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer_1 = Lecturer('Sherlock', 'Holmes')
cool_lecturer_2 = Lecturer('Doctor', 'Vatson')
cool_lecturer_1.courses_attached += ['Deduction']
cool_lecturer_2.courses_attached += ['Surgery']
 
cool_reviewer.rate_hw(best_student_1, 'Python', 7)
cool_reviewer.rate_hw(best_student_1, 'Python', 8)
cool_reviewer.rate_hw(best_student_1, 'Python', 5)
cool_reviewer.rate_hw(best_student_2, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 3)

best_student_1.rate_lc(cool_lecturer_1, 'Deduction', 10)
best_student_1.rate_lc(cool_lecturer_1, 'Deduction', 9)

best_student_1.rate_lc(cool_lecturer_2, 'Surgery', 10)
best_student_1.rate_lc(cool_lecturer_2, 'Surgery', 7)


print(cool_reviewer)
print(cool_lecturer_1)
print(cool_lecturer_2)
print(best_student_1)
print(cool_lecturer_1.average() < cool_lecturer_2.average())
print(best_student_1.average() < best_student_2.average())
print()

def students_average_hw(students, course):
  total_sum = 0
  for student in students:
    for keys, values in student.grades.items():
      if keys == course:
        total_sum += sum(values)/len(values)
  return total_sum/len(students)

print(students_average_hw([best_student_1, best_student_2], 'Python'))
  
def lecturer_average(list_lect):
  total_sum = 0
  for lecturer in list_lect:
    for values in lecturer.grades.values():
      total_sum += sum(values)/len(values)
  return total_sum/len(list_lect)

print(lecturer_average([cool_lecturer_1, cool_lecturer_2]))
