import random
import string
msg=input("Enter the length password u want to generate :")

# check that  password length must not be alphabets

if msg.isalpha():
    print("Enter password length only in digits")


elif not msg.isdigit():
    print("Only numbers are allowed for password length.")



else:
    msg_int = int(msg)          #   -----------      converting input that we have taken into integer

    if msg_int <= 0:
        print("Password length must be positive ")
 
    

    gen_no=random.choices(string.digits+string.ascii_lowercase+string.ascii_uppercase+string.punctuation,k=msg_int)
    print("Generated password are\n"+"".join(gen_no))
