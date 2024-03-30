guest_list = ["Rinoa, Marwa, Alia, sofia"]

# Printing a message that only two people can be invited
print("Sorry, but due to limited space, I can only invite two people for dinner.")

# Removing guests from the list until only two names remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I won't be able to invite you to dinner.")

# Printing invitation messages to the remaining guests
for guest in guest_list:
    print(f"Dear {guest},\nYou are still cordially invited to dinner at my place.\n\nBest regards,\n[Malaika Noor]")

# Removing the last two names from the list
del guest_list[:]

# Printing to verify the list is empty
print("Guest list after clearing:", guest_list)
