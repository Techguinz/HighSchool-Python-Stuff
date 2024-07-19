#create a id 

#ask user if they r student or teacher
#ask user for firstname and surname
#if teacher id= first 2  letters of first name and last 3
#of surname
#if student last 3 of firstname and first 2 letters 
#of surname

firstname=input("Enter your first name: ")
surname=input("Enter your surname: ")
role=input("r u a teacher or student: ")

if role=="teacher":
    username=(firstname[0:2] + surname[-3:]) #-3 to get last 3 letters of surname
                                         #index -0,-1,-2
else:
    role=="student"
    username=(firstname[-3:] + surname[0:2]) #-3 to get last 3 letters of surname
print("Your username is: " + username)