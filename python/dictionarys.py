#stores key value pairs

#customer={
    #"name": "John Smith",
   # "age": 30,
   # "is_verified": True
#}
#print(customer["name"])#grab name from customers in the dictionary

customer={
    "name": "John Smith",
    "age": 30,
    "is_verified": True#dictionaries are stored in speech marks
}

customer["name"]= "bob"#changes the name
print(customer.get("birthdate", "Jan 1 1980"))#ads birthdate to the customer
print("name")