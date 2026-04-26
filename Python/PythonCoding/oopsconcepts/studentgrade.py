from student import Student
from indriver import Indriver

class StudentGrade(Student,Indriver):
    def show_grade(self):
        if self.marks >=80:
            print("Grade:A")
        elif self.marks >=60:
            print("Grade:B")
        elif self.marks >=40:
            print("Grade:C")
        else:
            print("Fail")


obj = StudentGrade()
obj.get_student()
obj.get_driver()
obj.show_student()
obj.show_driver()
obj.show_grade()

