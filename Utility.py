class VendingMachine:
    def __init__(vm):
        # list of items and its prices 
        vm.menu = {
            '1': {'item': 'Coke', 'price': 1.00},
            '2': {'item': 'Chips', 'price': 0.50},
            '3': {'item': 'Candy', 'price': 0.75},
            '4': {'item': 'Water', 'price': 1.25},
            '5': {'item': 'Nuts', 'price': 1.50},
            '6': {'item': 'Juice', 'price': 1.75},
            '7': {'item': 'Popcorn', 'price': 1.00},
            '8': {'item': 'Energy Drink', 'price': 2.00},
            '9': {'item': 'Crackers', 'price': 0.75},
            '10': {'item': 'Chocolate Bar', 'price': 1.00},
            '11': {'item': 'Soda', 'price': 1.50},
            '12': {'item': 'Tea', 'price': 1.00},
            '13': {'item': 'Gum', 'price': 0.50},
            '14': {'item': 'Fruit Snacks', 'price': 1.25},
            '15': {'item': 'Coffee', 'price': 1.75},
            '16': {'item': 'Granola Bar', 'price': 1.00},
            '17': {'item': 'Muffin', 'price': 2.00},
            '18': {'item': 'Bagel', 'price': 1.50},
        }
        vm.balance = 0.0
       
       # Displaying the Menu
    def show_menu(vm):
        print("Hey there! Check out what we've got on Noor's Vending Machine:")
        for code, details in vm.menu.items():
            print(f"{code}: {details['item']} - ${details['price']}")

       # Choosing an Item
    def choose_item(vm, code):
        if code in vm.menu:
            return vm.menu[code]
        else:
            print("Not Available")
            return None

      # Inserting Coins 
    def insert_coins(vm, coin):
        if coin in [0.05, 0.10, 0.25, 1.00]:
            vm.balance += coin
            print(f"Your total is now ${vm.balance:.2f}.")
        else:
            print("Not Acceptable")

       # Buying an Item 
    def buy_item(vm, item):
        if item:
            price = item['price']
            if vm.balance >= price:
                vm.balance -= price
                print(f"Here's your {item['item']}! Enjoy!")
                print(f"Remaining Balance: ${vm.balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Did you pick something?")

       #Returning Change
    def give_change(vm):
        if vm.balance > 0:
            print(f"Returning change: ${vm.balance:.2f}")
            vm.balance = 0
        else:
            print("No change to return.")

   #Main Function
def main():
    vending_machine = VendingMachine()
    
    while True:
        vending_machine.show_menu()

        selected_code = input("Enter the code for your snack or 'exit' to leave: ").strip()
        if selected_code.lower() == 'exit':
            break

        selected_item = vending_machine.choose_item(selected_code)
        
        # If you've chosen, time to pay!
        if selected_item:
            # Drop in your coins
            while True:
                inserted_coin = input("Toss in your coins (0.05, 0.10, 0.25, 1.00) or 'done' when you're finished: ").strip()
                if inserted_coin.lower() == 'done':
                    break
                try:
                    coin_value = float(inserted_coin)
                    vending_machine.insert_coins(coin_value)
                except ValueError:
                    print("Invalid coin value. Please enter a valid coin or 'done'.")

            # Buying time!
            vending_machine.buy_item(selected_item)

            # Any change coming your way?
            vending_machine.give_change()
    
    print("Thank you for using Noor's Vending Machine. Have a great day!")

if __name__ == "__main__":
    main()


