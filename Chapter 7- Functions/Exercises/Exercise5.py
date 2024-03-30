def describe_city(city, country = "USA"):
    msg = f"My favourite city in {country} is {city}."
    print (msg)

#calling function
describe_city(city= "new york")

#cleaning up output
print ("\n")

#calling function with different city
describe_city(city= "chicago")

#cleaning up output
print ("\n")

#calling function with new country
describe_city("paris","frace")
