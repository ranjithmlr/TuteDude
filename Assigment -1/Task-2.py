# 1. Take the user's first and last name as input
# We use the input() function to get data from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# 2. Concatenate the first name and last name into a full name
# We add a space " " between them so they don't stick together
full_name = first_name + " " + last_name

# 3. Print a personalized greeting message
# We use an f-string (formatted string) to insert the full_name variable
print(f"Hello, {full_name}! Welcome to the Python program.")