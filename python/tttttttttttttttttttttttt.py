# List of existing friends
friends = ["callum", "ethan", "bob", "oliwier"]

# Ask for the user's name
name1 = input("What is your name? ")

# Check if the user's name is in the list of friends
if name1 in friends:
    print("My friend's name is", name1)
else:
    print(f"Nice to meet you, {name1}!")

# Define favorite numbers
firstfav = 9
secondfav = 23

# Set the number of attempts allowed
attempts = 5

# Get user's guesses for favorite numbers
num1 = int(input("Guess my first favorite number: "))
num2 = int(input("Guess my second favorite number: "))

# Loop for guessing favorite numbers with attempts counter
while (num1 != firstfav or num2 != secondfav) and attempts > 1:
    attempts -= 1
    if num1 != firstfav and num2 != secondfav:
        print(f"Both numbers are incorrect. You have {attempts} attempts left.")
    elif num1 != firstfav:
        print(f"First number is incorrect. You have {attempts} attempts left.")
    elif num2 != secondfav:
        print(f"Second number is incorrect. You have {attempts} attempts left.")
    
    num1 = int(input("Guess my first favorite number: "))
    num2 = int(input("Guess my second favorite number: "))

# Check if the guessed favorite numbers are correct
if num1 == firstfav and num2 == secondfav:
    print(f"You guessed my favorite numbers correctly, {name1}!")
else:
    print("Sorry, you've used all your attempts. The correct numbers are:", firstfav, "and", secondfav)

# Ask if the user wants to be a friend
friends1 = input("Do you want to be my friend? (y/n): ")

# Handle user's response to becoming a friend
if friends1 == "y":
    friends.append(name1)
    print(f"{name1} is now my friend!")
    print("My friends are now:", friends)
elif friends1 == "n":
    print("You are not my friend!")
else:
    print("Invalid input, please retry.")
    friends1 = input("Do you want to be my friend? (y/n): ")

    # Retry the friend confirmation step
    if friends1 == "y":
        friends.append(name1)
        print(f"{name1} is now my friend!")
        print("My friends are now:", friends)
    elif friends1 == "n":
        print("You are not my friend!")
    else:
        print("Sorry, you've provided an invalid response. Goodbye.")
