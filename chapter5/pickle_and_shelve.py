import pickle
import shelve

# x = 10
# y = [1, 2, 3, 4, 5]
# z = {"name": "Alice", "age": 30}


# def save_data():
#     global x, y, z
#     data = {"x": x, "y": y, "z": z}

#     with open("chapter5/data.pkl", "wb") as pkl_file:
#         pickle.dump(data, pkl_file)


# save_data()

# x = None
# y = None
# z = None


# def load_data():
#     global x, y, z

#     with open("chapter5/data.pkl", "rb") as pkl_file:
#         data = pickle.load(pkl_file)

#     x = data["x"]
#     y = data["y"]
#     z = data["z"]


# load_data()

# print(x)
# print(y)
# print(z)


integers1 = [1, 2, 3, 4, 5]
integers2 = [6, 7, 8, 9, 10]

with shelve.open("chapter5/data_shelve", "c") as db:
    db["integers1"] = integers1
    db["integers2"] = integers2

with shelve.open("chapter5/data_shelve", "r") as db:
    for key in db.keys():
        print(f"{key}: {db[key]}")
