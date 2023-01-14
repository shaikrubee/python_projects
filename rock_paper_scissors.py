import random

possible_option=["rock","paper","scissors"]

while True:
    user_option=input().lower()
    
    random_number=random.randint(0,2)
    computer_option=possible_option[random_number]
    print(computer_option)

    if user_option not in possible_option:
        continue

    if user_option==computer_option:
        print("Game Tie")

    elif user_option=="rock":
        if computer_option=="scissors":
            print("User Wins")
        else:
            print("Computer wins")
    elif user_option=="paper":
        if computer_option=="scissors":
            print("Computer Wins") 
        else:
            print("User Wins")
    elif user_option=="scissors" :
        if computer_option=="rock":
            print("Computer wins") 
        else:
            print("User Wins")  

    play_again=input("Play again? (y/n):")

    if play_again.lower()!="n":
        break





