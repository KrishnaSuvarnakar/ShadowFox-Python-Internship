class Person:

    def show_name(self):
        print("My name is Krishna")


class Student(Person):

    def show_branch(self):
        print("My branch is AIML")


student = Student()

student.show_name()
student.show_branch()