"""
DATA 200 Fall 2019 Homework 6
Courtney Nguyen
10NOV19
hw7-1.py

"""

class Person:

    def __init__(self, fname, lname, id): ## constructor to initialize object
        self.fname = fname
        self.lname = lname
        self.id = id

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def describe(self):
        return self.fullname(), self.id

class Student(Person):
    
    def __init__(self, fname, lname, id, student_type, cls = []):
        super().__init__(fname, lname, id)

        if student_type.lower() == "undergraduate" or student_type.lower() == "graduate":
            self.student_type = student_type
        else:
            self.student_type = "invalid type entered"

        self.cls = cls

    def enroll(self, class_enroll):
        self.cls.append(class_enroll)

    def describe(self):
        return self.fullname(), self.id, self.student_type, self.cls

class Staff(Person):

    def __init__(self, fname, lname, id, staff_type):
        super().__init__(fname, lname, id)

        if staff_type.lower() == "temporary" or staff_type.lower() == "permanent":
            self.staff_type = staff_type
        else:
            self.student_type = "invalid type entered"

    def describe(self):
        return self.fullname(), self.id, self.staff_type

class Faculty(Person):

    def __init__(self, fname, lname, id, faculty_type, cls_taught =[]):
        super().__init__(fname, lname, id)

        if faculty_type.lower() == "full-time" or faculty_type.lower() == "part-time":
            self.faculty_type = faculty_type
        else:
            self.faculty_type = "invalid type entered"

        self.cls_taught = cls_taught

    def assign_class(self, cls):
        self.cls_taught.append(cls)

    def describe(self):
        return self.fullname(), self.id, self.faculty_type, self.cls_taught

p1 = Person('Courtney', 'Nguyen', '0001')
print(p1.describe())

p2 = Student('Luu', 'Votran', '0002','GRADUATE')
p2.enroll('PE')
p2.enroll('DATA200')
p2.enroll('Underwater Basket Weaving')
print(p2.describe())

p3 = Staff('Courtney', 'Nguyen', '0003', 'temporary')
print(p3.describe())

p4 = Faculty('Luu', 'Votran', '0004', 'FULL-time')
p4.assign_class('pottery')
p4.assign_class('flat earth theory')
print(p4.describe())