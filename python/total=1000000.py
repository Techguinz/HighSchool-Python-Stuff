total=1000000
print('The price of the house is $1,000,000.')
credit = input('How good is your credit score? ')
if credit == 'good':
    print('BERRY GOOD, the down payment is $100,000 so ur total is', "$",total-100000)
elif credit == 'bad':
    print('BERRY BAD, the down payment is $200,000 so ur total is', "$",total-200000)
else:
    print("I don't, you cant buy this house")
