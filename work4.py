class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grade_list in self.grades.values():
            all_grades.extend(grade_list)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        avg = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress:
            return 'Ошибка'
        if course not in lecturer.courses_attached:
            return 'Ошибка'
        if not (1 <= grade <= 10):
            return 'Ошибка'
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]

    def average_grade(self):
        all_grades = []
        for grade_list in self.grades.values():
            all_grades.extend(grade_list)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        avg = self.average_grade()
        courses_str = ', '.join(self.courses_in_progress)
        finished_str = ', '.join(self.finished_courses)
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg}\n"
            f"Курсы в процессе изучения: {courses_str}\n"
            f"Завершенные курсы: {finished_str}"
        )

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


def average_hw_grade(students, course_name):
    all_grades = []
    for student in students:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if not all_grades:
        return 0
    return sum(all_grades) / len(all_grades)

def average_lecture_grade(lecturers, course_name):
    all_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if not all_grades:
        return 0
    return sum(all_grades) / len(all_grades)


# Создаем по 2 экземпляра каждого класса
student1 = Student('Ruoy', 'Eman', 'M')
student2 = Student('Anna', 'Smith', 'F')

lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('Other', 'Person')

reviewer1 = Reviewer('John', 'Doe')
reviewer2 = Reviewer('Jane', 'Smith')

#  Добавляем курсы
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student2.courses_in_progress = ['Python', 'Java']

lecturer1.courses_attached = ['Python', 'Git']
lecturer2.courses_attached = ['Python', 'Java']

reviewer1.courses_attached = ['Python', 'Git']
reviewer2.courses_attached = ['Python', 'Java']

# Вызываем методы
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 8)

student1.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 7)

# Тестируем магические методы
print("Сравнение студентов:", student1 > student2)
print("Сравнение лекторов:", lecturer1 < lecturer2)

# Тестируем функции
print("Средняя оценка за ДЗ по Python:", average_hw_grade([student1, student2], 'Python'))
print("Средняя оценка за лекции по Python:", average_lecture_grade([lecturer1, lecturer2], 'Python'))
print("Средняя за ДЗ по Java:", average_hw_grade([student1, student2], 'Java'))