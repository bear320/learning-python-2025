# Ask user's name
# Ask how much money they have
# Ask them whether they are hungry
# Check if they have enough money ($30) to buy breakfast
# If they are hungry and have enough money, print "You can buy breakfast!"
# Else, print "You don't have enough money for breakfast."

name = input("What is your name? ")  # string
money = float(input("How much money do you have? "))  # float
hungry = input("Are you hungry? (Y/N) ")  # string

if hungry == "Y":
    if money >= 30:
        print(f"Hello {name}, you can buy breakfast!")
    else:
        print(f"Hello {name}, you don't have enough money for breakfast.")
elif hungry == "N":
    if money >= 30:
        print(f"Hello {name}, you have enough money, but you are not hungry.")
    else:
        print(f"Hello {name}, you don't have enough money, and you are not hungry.")
else:
    print("Invalid input for hunger status. Please enter 'Y' or 'N'.")
