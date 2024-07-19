secret_num=9
guess_count=0
guess_limit=3
while guess_count <guess_limit:
    guess=int(input("Guess a number between 1 and 10: "))
    guess_count+=1
    if guess==secret_num:
        print("You got it!")
        break
else:
    print("you failed")
    
