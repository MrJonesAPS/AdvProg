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
Student1 = Student("student1", 15, 10)
Teacher1 = Teacher("Teacher1",45,"Math")

print(Student1)
print(Teacher1)
