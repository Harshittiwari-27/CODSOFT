#                                         Calculator logic and everthing will be here :-
try:
       
    num1=float(input("Enter the first no :\n"))
    num2=float(input("Enter the second no :\n"))
except ValueError:                          # If user input other than number it will throw  ERROR !!
       print(" ERROR !!  Please enter the numbers only :")
       exit()
       


#                                          Menu for operation choices :-
print("\n--- Simple Calculator ---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice to do perform the above operation that is  (1/2/3/4): ")

#                                          Opreations that to be performed :-

if choice == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
elif choice == '3':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
elif choice == '4':
        if num2 == 0:
            print("Error !!  Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
else: 
        print("Invalid choice. Please select only from 1, 2, 3, or 4.")

# YOUR OUTPUT WILL BE DISPLAYED ON THE SCREEN :-