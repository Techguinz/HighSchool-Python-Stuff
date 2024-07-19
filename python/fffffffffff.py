friends = ["callum", "ethan", "bob", "oliwier"]
name1 = input("What is your name? ")

if name1 in friends:
    print("My friend's name is", name1)
else:
    print(f"Nice to meet you, {name1}!")

firstfav = 9
secondfav = 23

num1 = int(input("Guess my first favorite number: "))
num2 = int(input("Guess my second favorite number: "))

while num1 != firstfav or num2 != secondfav:
    num1 = int(input("Guess my first favorite number: "))
    num2 = int(input("Guess my second favorite number: "))
    
if num1 == firstfav and num2 == secondfav:
    print(f"You guessed my favorite numbers correctly, {name1}!")
   

 friends1=input("wanna be my friend. y/n"):
    if friends1 == "y":
    print(names.append(name1))
    else:
    print(f"{name1} is not my friend!")
    





