print("---------- MINI CALCULATOR ----------")
num1=float(input("enter 1st number: "))
num2=float(input("enter 2nd number: "))
print("Operations are:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter a digit from 1-4 as mentioned above: "))
if choice == 1:
    print("The sum of given two numbers is : ",num1+num2)
elif choice == 2:
    print("The difference of given two numbers is : ",num1-num2)
elif choice == 3:
    print("The product of given two numbers is : ",num1*num2)
elif choice == 4:
    print("The division of given two numbers is : ",num1/num2)
else:
    print("Invalid digit enetered")