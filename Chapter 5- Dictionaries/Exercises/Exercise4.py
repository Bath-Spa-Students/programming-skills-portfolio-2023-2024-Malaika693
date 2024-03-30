rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

# Print sentences about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print names of each river
print("\nRivers:")
for river in rivers:
    print(river)

# Print names of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
