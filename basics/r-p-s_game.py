import random

def get_choice():
    player_choice = input("Enter choice: ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}
    return choices

choices = get_choice()
print(choices)

def check_win(player, computer):
    print(f"You chose {player} while computer chose {computer}")
    if player == computer:
        return "draw"
    elif player == "rock" and computer == "paper":
        return "computer won"
    elif player == "paper" and computer == "scissor":
        return "computer won"
    elif player == "scissor" and computer == "rock":
        return "computer won"
    else:
        return "player won"

result = check_win(choices["player"], choices["computer"])
print(result)
