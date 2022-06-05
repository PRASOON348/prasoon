name = input("")
if len(name) < 3:
    print("name must have greater than 3 characters")
elif len(name) > 50:
    print("name must have less than 50 characters")
else:
    print("good")