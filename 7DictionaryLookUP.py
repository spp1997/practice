# Sample dictionary of countries and their capitals
capitals = {
    "India": "New Delhi",
    "United States": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "Australia": "Canberra"
}

# Ask the user for a country name
country = input("Enter the country name: ").strip()

# Look up the country in a case‑insensitive way
capital = capitals.get(country) or capitals.get(country.title())

if capital:
    print(f"The capital of {country} is {capital}.")
else:
    print(f"Sorry, I don't have the capital for '{country}'.")