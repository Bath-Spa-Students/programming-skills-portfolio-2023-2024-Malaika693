guest_list = ["Rinoa", "Sofia", "Marwa"]

#guest who cant make it 
guest_cant_make_it = guest_list.pop(1)
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.")

# Adding a new guest to the list
new_guest = " Alia"
guest_list.append(new_guest)

# nvitation messages for each person still on the list
for guest in guest_list:
    print(f'''Dear {guest},\nYou are cordially invited to dinner at my place.
I would be honored to have you join me for an evening of delightful conversation and good food.
 \n\nBest regards,\n[Malaika noor]''')
