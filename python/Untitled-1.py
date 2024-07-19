friends=["callum","ethan","jessica","oliwier"]
name1=input("what is your name? ")
if name1==friends[0]:
    print("my friends called",friends[0])
elif name1==friends[1]:
    print("my friends called",friends[1])
elif name1==friends[2]:
    print("my friends called",friends[2])
elif name1==friends[3]:
    print("my friends called",friends[3])
else:
    print(f"nice to meet u {name1} ")

firstfav=(9)
secondfav=(23)

num1=int(input("guess my first favourite number: "))
num2=int(input("guess my second favourite number: "))

while num1!=firstfav + num2!=secondfav:
   
    num1=int(input("guess my first favourite number: "))
    num2=int(input("guess my second favourite number: "))
    if num1==9 + num2==23:
        print(f"u guessed my favourite numbers correctly {name1}")


