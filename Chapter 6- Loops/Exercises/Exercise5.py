# Create the sandwich_orders list
sandwich_orders = ['tuna', 'pastrami', 'turkey', 'ham', 'pastrami', 'vegetable', 'pastrami']

# Create the finished_sandwiches list
finished_sandwiches = []

# Print a message about running out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the sandwich_orders list
for sandwich in sandwich_orders:
    # Make the sandwich
    print("I made your", sandwich, "sandwich.")
    # Move it to the finished_sandwiches list
    finished_sandwiches.append(sandwich)

# Print the finished sandwiches
print("Here are the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

