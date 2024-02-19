import re

#Password must be atleast 8 char long
password = input("Enter your Password : ")

if len(password) < 8:
    print("Password must be atleast 8 characters long")
#Password must contain atleast one uppercase letter
elif not re.search("[A-Z]", password):
    print("Password must contain atleast one uppercase letter")
#Password must contain atleast one lowercase letter
elif not re.search("[a-z]", password):
    print("Password must contain atleast one lowercase letter")
#Password must contain atleast one number
elif not re.search("[0-9]", password):
    print("Password must contain atleast one number")
else:
    print("Password is Strong")
