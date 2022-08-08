import re

mobileNo=input("Enter Your 10 digit Mobile Number : ")

x=re.search("[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]",mobileNo)

if x:
    print("Entered Number is Valid...")

else:
    print("Entered Number is inValid...\n" "please enters format should be xxx-xxx-xxxx")
    

    
