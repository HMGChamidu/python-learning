class Student:
    university = "Sabaragamuwa University"
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")

    def change_course(self, new_course):
        self.course = new_course

    def change_name(self, new_name):
        self.name = new_name
    def show_marks()
student1 = Student("Chamidu", "CIS")
student1.university = "Another University"
student2 = Student("Terran", "IS")


student1.show_details()
student1.change_name("Alex")
student1.show_details()

student1.change_course("Software Engineering")

print("\nAfter changing the course:")
student1.show_details()

student2.show_details()
print(Student.university)
print(student1.university)
print(student2.university)