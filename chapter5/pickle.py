import pickle

x = 10
y = [1, 2, 3, 4, 5]
z = {"name": "Alice", "age": 30}

# with open("chapter5/data.pkl", "wb") as pkl_file:  # Write binary mode
#     pickle.dump(x, pkl_file)
#     pickle.dump(y, pkl_file)
#     pickle.dump(z, pkl_file)

with open("chapter5/data.pkl", "rb") as pkl_file:  # Read binary mode
    x_loaded = pickle.load(pkl_file)
    y_loaded = pickle.load(pkl_file)
    z_loaded = pickle.load(pkl_file)
    print(x_loaded)
    print(y_loaded)
    print(z_loaded)
