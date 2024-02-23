# user_input.py

# Ask user for name
name = input("What is your name? ")

# Ask user for age
age = input("How old are you? ")

# Ask user for location
location = input("Where are you located? ")

# Print out a personalized message using the user's name, age, and location
print("Hello {}, you are {} years old and you live in {}.".format(
    name, age, location))
