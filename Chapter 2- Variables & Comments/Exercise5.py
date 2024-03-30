budget = 50 #total money
usb_price = 6 #price of each usb

## Calculate the maximum number of USB sticks can be bought 
usbamount = int(budget/usb_price)
#Calculate the remaing amount 
remaining = budget - (usbamount*usb_price)
#print the result
print(f"She can buy {usb_price} USB sticks and will have £{remaining} left.")
