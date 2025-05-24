if True:
    print("This is true")

if False:
    print("This is true")
else:
    print("This is false")

# age < 8: free
# age >= 8 and age < 65: pay full price
# age >= 65: pay half price

age = 18

if age < 8:
    print("Free")
elif age >= 8 and age < 65:
    print("Pay full price")
else:
    print("Pay half price")


if (5 > 3) and []:
    print("The condition is true")
else:
    print("The condition is false")
