class Robot:
    def __init__(self, name):
        self.name = name
        self.__serial_number = "SN123456"  # Private attribute

    def get_info(self):
        print(f"Robot Name: {self.name} | Serial Number: {self.__serial_number}")

    # getter & setter (unusual in Python, but shown for demonstration)
    def get_serial_number(self):
        print(f"Serial Number: {self.__serial_number}")

    def set_serial_number(self, serial_number):
        self.__serial_number = serial_number
        print(f"Serial Number updated to: {self.__serial_number}")

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
