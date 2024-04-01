import random

user_score = 0
computer_score = 0

while True:

    user_input = input("Please enter Rock/Paper/Scissors or Press 'q' to quit: ").lower()
    if user_input == "q" :
        print("Thanks for playing")
        break
    elif user_input not in ["rock", "paper", "scissors"]:
        continue
    else:
        computer_input = random.choice(["rock","paper","scissors"])

        if user_input ==  "rock" and  computer_input=="scissors" or user_input == "paper" and computer_input == "rock" or user_input == "scissors" and computer_input == "paper":
            print("You won")
            user_score +=1
        else:
            print("Computer won")
            computer_score+=1
        print(f"your score: {user_score}")        
        print(f"computer score: {computer_score}")