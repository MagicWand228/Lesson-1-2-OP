class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age




    def greeting(self):
        print(f"hello i am {self.name}")

    def grow_up(self):
        self.age = self.age + 1

    def print_age(self):
        print(f"age - {self.age}")

Maksum_student = Student(name = "Maxym", age = 12)
Maksum_student.greeting()

matvii_student = Student(name = "Matvii", age = 14)
matvii_student.greeting()

Maksum_student.print_age()
Maksum_student.grow_up()
Maksum_student.print_age()