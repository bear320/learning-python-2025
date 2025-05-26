# Structural Pattern Matching

lang = input("What programming language do you want to learn? ")

match lang:
    case "JavaScript":
        print("You'll become a frontend developer!")
    case "PHP":
        print("You'll become a backend developer!")
    case "Python":
        print("You'll become a data scientist!")
    case "Kotlin":
        print("You'll become an Android developer!")
    case "Swift":
        print("You'll become an iOS developer!")
    case _:
        print(f"You'll become a {lang} developer!")

weekday = input("What day of the week is it? ")

match weekday:
    case "Sunday" | "Monday":
        print("Closed today!")
    case "Saturday":
        print("Open from 10 AM to 4 PM!")
    case _:
        print("Open from 8 AM to 5 PM!")

command = input("Where do you want to go? ")

match command.split(" "):
    case ["Go", "home"]:
        print("You are going home!")
    case _:
        print("You are going somewhere else!")
