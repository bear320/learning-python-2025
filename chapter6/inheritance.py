class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Student(People):
    def __init__(self, name, age, student_id):
        # People.__init__(self, name, age)
        super().__init__(name, age)
        self.student_id = student_id

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")


Oliver = Student("Oliver", 20, "S12345")
print(Oliver.name)
Oliver.eat("pizza")
