class Robot:
    def __init__(self, name):
        self.name = name
        self.__serial_number = "SN123456"  # Private attribute
        self.__useful_life = 10  # Private attribute in years

    def get_info(self):
        print(f"Robot Name: {self.name} | Serial Number: {self.__serial_number}")

    # getter & setter (unusual in Python, but shown for demonstration)
    def get_serial_number(self):
        print(f"Serial Number: {self.__serial_number}")

    def set_serial_number(self, serial_number):
        self.__serial_number = serial_number
        print(f"Serial Number updated to: {self.__serial_number}")

    def useful_life_getter(self):
        print(f"Useful Life: {self.__useful_life} years")

    def useful_life_setter(self, new_life):
        if new_life > 0:
            self.__useful_life = new_life
            print(f"Useful Life updated to: {self.__useful_life} years")
        else:
            print("Useful life must be positive.")

    # private method
    def __private_greet(self):
        print("Greeting from the private method!")

    def greet(self):
        print("Greeting from the public method!")
        self.__private_greet()


my_robot = Robot("Robo1")
print(my_robot.name)  # Output: Robo1
# print(my_robot.__serial_number)  # Output: AttributeError
my_robot.get_info()  # Output: Serial Number: SN123456
my_robot.get_serial_number()  # Output: Serial Number: SN123456
my_robot.set_serial_number("SN654321")  # Output: Serial Number updated to: SN654321
# my_robot.__private_greet()  # Output: AttributeError
my_robot.greet()  # Output: Greeting from the public method! \n Greeting from the private method!
my_robot.useful_life_getter()  # Output: Useful Life: 10 years
my_robot.useful_life_setter(15)  # Output: Useful Life updated to: 15 years
