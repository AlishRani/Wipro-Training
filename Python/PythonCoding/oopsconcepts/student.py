class Student:
    def get_student(self):
        self.name = input("Enter name:")
        self.marks = int(input("Enter marks: "))

    def show_student(self):
        print("Name:",self.name)
        print("Marks:",self.marks)