import random

while True:
    userCho = input(
        "Make a Choice between \n P for Paper \n R for Rock and \n S for Scissors \n \n")

    userChoice = userCho.lower()

    if userChoice == "r":
        userChoice = "Rock"
    elif userChoice == "s":
        userChoice = "Scissors"
    elif userChoice == "p":
        userChoice = "Paper"

    possibleChoice = ["Rock", "Paper", "Scissors"]
    computerChoice = random.choice(possibleChoice)

    if userChoice in possibleChoice:
        print(
            f"\n Player {userChoice} : CPU {computerChoice} \n")
        if userChoice == "Paper" and computerChoice == "Rock":
            print("\n You are the Winner \n")
            break
        elif userChoice == "Paper" and computerChoice == "Scissors":
            print("\n Computer is the Winner \n")
            break
        elif userChoice == "Rock" and computerChoice == "Paper":
            print("\n Computer is the Winner \n")
            break
        elif userChoice == "Rock" and computerChoice == "Scissors":
            print("\n You are the Winner \n")
            break
        elif userChoice == "Scissors" and computerChoice == "Rock":
            print("\n Computer is the Winner \n")
            break
        elif userChoice == "Scissors" and computerChoice == "Paper":
            print("\n You are the Winner \n")
            break
        else:
            print("It is a tie \n \n \n")

    else:
        print("Please choose between the correct Data")
