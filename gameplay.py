import random

def play_game():
    choices = ["rock", "paper", "scissors"]

    while True:
        print("\n--- Rock Paper Scissors Game ---")
        print("1. Play Game")
        print("2. Exit")

        option = input("Enter your choice: ").strip()

        if option == "1":
            user = input("Choose Rock, Paper, or Scissors: ").strip().lower()

            if user == "scissor":
                user = "scissors"

            if user not in choices:
                print("Invalid choice! Try again.")
                continue

            computer = random.choice(choices)
            print("Computer chose:", computer)

            if user == computer:
                print("It's a Tie!")
            elif (
                (user == "rock" and computer == "scissors") or
                (user == "paper" and computer == "rock") or
                (user == "scissors" and computer == "paper")
            ):
                print("You Win!")
            else:
                print("Computer Wins!")

        elif option == "2":
            print("Thank you for playing!")
            break

        else:
            print("Invalid menu option!")

play_game()