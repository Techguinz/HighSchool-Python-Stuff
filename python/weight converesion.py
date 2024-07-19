#Write a algorithm that uses iteration to allow Taylor to:
#• enter 10 values
#• count how many values are over 50
#• output the count of values over 50 after all 10 values are entered

count=0#start num
for i in range(10):#• enter 10 values
    num=int(input("Enter a number: "))
    if num>50:#• count how many values are over 50
        count+=1
print(count)#output count of values over 50 after all 10 values are entered