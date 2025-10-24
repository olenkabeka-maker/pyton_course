# Task 1     School

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):                                                  
        print(f"Привіт! Мене звати {self.name}, мені {self.age} років.")

    def is_adult(self):
        return self.age >= 18

class Student(Person):                                # підклас для учнів школи
    
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
        self.courses = []
        self.attendance = 0                           # відвідування учнями

    def enroll_course(self, course_name):             # зарахування на курс
        self.courses.append(course_name)
        print(f"{self.name} записався на курс {course_name}.")

    def attend_class(self):
        self.attendance += 1
        print(f"{self.name} відвідав урок. Загальна кількість відвідувань: {self.attendance}")

    def study(self, subject):
        print(f"{self.name} зараз вивчає {subject}.")

    def get_info(self):
        return f"Учень {self.name}, клас: {self.grade}, курси: {', '.join(self.courses) or 'ще не обрано'}"

class Teacher(Person):                                 # підклас для вчителів
   
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
        self.students = []

    def add_student(self, student):                    # додавання учнів до класу
    
        if isinstance(student, Student):
            self.students.append(student)
            print(f"{student.name} додано до класу вчителя {self.name}.")
        else:
            print("Можна додати лише учня.")

    def teach(self):
        print(f"{self.name} викладає предмет {self.subject}.")

    def grade_student(self, student, grade):
        
        if student in self.students:
            print(f"{self.name} поставив(ла) {student.name} оцінку {grade} з предмету {self.subject}.")
        else:
            print(f"{student.name} не є учнем {self.name}.")

    def get_info(self):
        return f"Вчитель {self.name}, предмет: {self.subject}, зарплата: {self.salary} грн."


teacher = Teacher("Альона Вікторівна", 39,"Англійська мова", 17000)
student1 = Student("Дмитро", 16, "Д24", 10)
student2 = Student("Аня", 16, "А02", 10)

teacher.add_student(student1)
teacher.add_student(student2)
teacher.teach()

student1.enroll_course("Математика")
student1.study("Математика")
student1.attend_class()

print()
print(teacher.get_info())
print(student1.get_info())
print(student2.get_info())