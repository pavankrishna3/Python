import random

print("Do you want to guess the number i  am thinking of?")
ans = input("Yes or No: ")

if ans == "yes"or"yes":
    
    print("what is the upper limit?")
    uplimit=input("Enter an integer :")

    if uplimit.isdigit():
        uplimit=int(uplimit)
        if uplimit <= 0:
            print("select a number  greater than zero.")
        else:
            rand = random.randint(1,uplimit)
    else:
        print("please enter a number.")
else:
    quit()

guesses=0
while True:
    guesses += 1
    num = int(input("Enter your guess :"))
    if rand == num:
        print(f"You take {guesses} attempts to guess the number")
        break
    else:
        if rand>num:
            print("Higher")
        else:
            print("Lower")
