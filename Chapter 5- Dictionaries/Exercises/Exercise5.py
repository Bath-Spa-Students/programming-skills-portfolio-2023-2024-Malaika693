# Create dictionaries representing different pets
pet1 = {'kind': 'dog', 'owner': 'Alice', 'age': 3, 'color': 'brown'}
pet2 = {'kind': 'cat', 'owner': 'Bob', 'age': 5, 'color': 'black'}
pet3 = {'kind': 'rabbit', 'owner': 'Charlie', 'age': 2, 'color': 'white'}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Pet: {pet['kind']}")
    print(f"Owner: {pet['owner']}")
    print(f"Age: {pet['age']} years")
    print(f"Color: {pet['color']}")
    print()  

