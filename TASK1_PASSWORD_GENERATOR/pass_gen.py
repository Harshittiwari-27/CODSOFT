import random
import string
msg=int(input("Enter the length password u want to generate :"))
# print(string.digits[:msg])

gen_no=random.choices(string.digits,k=msg)
print("".join(gen_no))
