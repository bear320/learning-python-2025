person = {
    "name": "Oliver",
    "age": 27,
    "contacts": {"phone": "123-456-789", "email": "myemail@example.com"},
}
print(person)  # {'name': 'Oliver', 'age': 27}
print(person["name"])  # Oliver
print(person["age"])  # 27
print(person["contacts"]["phone"])  # 123-456-789
print(person["contacts"]["email"])  # myemail@example.com

person["name"] = "Robert"
print(person["name"])  # Robert
