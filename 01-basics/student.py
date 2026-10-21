class student:
    def __init__(self,name,course):
        self.name = name
        self.course = course

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")

    def change_course(self, new_course):
        self.course = new_course
        
    def change_name(self, new_name):
        self.name = new_name

student1 = student("Chamidu", "CIS")
student2 = student("Terran", "IS")

student1.show_details()
student1.change_name("Alex")
student1.show_details()

student1.change_course("Software Engineering")

print("\nAfter changing the course:")
student1.show_details()

student2.show_details()