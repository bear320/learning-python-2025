class Employee:
    def __init__(self):
        self.income = 0
        # self.__tax = 0

    def earn(self, amount):
        self.income += amount
        # self.__tax = self.income * 0.05

    # def get_tax(self):
    #     return self.__tax

    @property
    def tax(self):
        return self.income * 0.05

    @tax.setter
    def tax(self, value):
        self.income = value / 0.05


Oliver = Employee()
Oliver.earn(300)
# print("Tax:", Oliver.get_tax())
Oliver.earn(500)
# print("Tax:", Oliver.get_tax())
print("Tax:", Oliver.tax)
Oliver.tax = 1000
print("Income after setting tax to 1000:", Oliver.income)
