#  list of places to visit
places_to_visit = ["New york", "Paris", "Germany", "London", "Maldives"]

# Print  list
print(" order:")

# Print list in alphabetical order 
print("Alphabetical order:", sorted(places_to_visit))

# Confirm  order is preserved
print(" order:")

# Print list in reverse alphabetical order 
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Confirm  order is preserved
print(" order:")

# Change the order of the list using reverse()
places_to_visit.reverse()
print("Reversed order:")

# Change the order back to  using reverse()
places_to_visit.reverse()
print("Back to  order:")

# Sort the list in alphabetical order using sort()
places_to_visit.sort()
print("Sorted in alphabetical order:")

# Sort the list in reverse alphabetical order using sort()
places_to_visit.sort(reverse=True)
print("Sorted in reverse alphabetical order:")
