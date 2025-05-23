print(10 / 0)  # ZeroDivisionError

if 2 or (10 / 0):
    print("We got no error")  # We got no error

if (10 / 0) or 2:
    print("We got no error")  # ZeroDivisionError
