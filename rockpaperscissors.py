import random
user_choice=int(input("Enter your choice:\n1 for Rock\n2 for Paper\n3 for Scissors:"))
if user_choice >= 4 or user_choice < 1:
    print("You entered invalid number,You lose.")
else:
    computer_choice=random.randint(1,3)
    print("Computer Chose : ")
    print(computer_choice)
    if computer_choice == user_choice:
        print("Its a draw.")
    elif computer_choice == 1 and user_choice == 3:
        print("You Lose.")
    elif user_choice == 1 and computer_choice == 3:
        print("You Win.")
    elif computer_choice  > user_choice:
        print("You Lose.")
    elif user_choice > computer_choice:
        print("You Win.")
