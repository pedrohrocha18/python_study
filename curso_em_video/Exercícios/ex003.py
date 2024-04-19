# Make program that read something typed on keyboard, your type primitive and all informations possibles about it.

data = input("Type something:\n")

print("What did you type:", data)
print("The type is:", type(data))
print("The length is:", len(data), "characters.")
print("The data is alpha?", data.isalpha())
print("The data is numeric?", data.isnumeric())
print("The data is digit?", data.isdigit())
