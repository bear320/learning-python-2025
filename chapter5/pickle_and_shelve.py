import pickle

# x = 10
# y = [1, 2, 3, 4, 5]
# z = {"name": "Alice", "age": 30}


# def save_data():
#     global x, y, z
#     data = {"x": x, "y": y, "z": z}

#     with open("chapter5/data.pkl", "wb") as pkl_file:
#         pickle.dump(data, pkl_file)


# save_data()

x = None
y = None
z = None


def load_data():
    global x, y, z

    with open("chapter5/data.pkl", "rb") as pkl_file:
        data = pickle.load(pkl_file)

    x = data["x"]
    y = data["y"]
    z = data["z"]


load_data()

print(x)
print(y)
print(z)
