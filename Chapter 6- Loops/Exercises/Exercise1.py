topping_list = ['chicken','beef','capsicum','olives','bell pepper','tomatoes','cheese','peperroni' ]

print("Type 'quit' to finish adding toppings")

# While loop for inputting toppings
while True:
    pizza_toppings = input("Enter a pizza topping: ").strip()

    # Setting a break for the loop and using append to add toppings into list
    if pizza_toppings.lower() == 'quit':
        break
    else:
        topping_list.append(pizza_toppings)
        print(f"{pizza_toppings} will be added to your pizza.")

# Printing all toppings added
print("Your pizza will be topped with:", topping_list)
