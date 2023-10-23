###############################
# Program Name: School People
# Written By: Mr. Jones
# Date: Oct 2023
# Purpose: For in-class demonstration on  inheritance
#
################################

#Imports

#Define Classes
class SchoolPeople:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def __str__(self):
        return self.__name + " is a " \
        + type(self).__name__ \
        + " who is " \
        + str(self.age) + " years old"

class Student(SchoolPeople):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade  = grade

class Teacher(SchoolPeople):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject  = subject

#main
student1 = Student("Student1", 15, 10)
teacher1 = Teacher("Teacher1",45,"Math")

print(student1)
print(teacher1)
