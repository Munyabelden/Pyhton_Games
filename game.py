import random

def play():
    user = input("Choose one -> 'r' for rock, 's' for scissors and 'p' for paper: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a Tie!"

    if is_win(user, computer):
        return "You won!!!"
    
    return "You're a LOSER"

def is_win(player, opponent):
    if player == 'r' and opponent == 's' or player == 'p' and opponent == 'r' or player == 's' and opponent == 'p':
        return True

print(play())
# def is_loser(player, opponent):
#     if player == 'r' and opponent == 'p' or player == 'p' and opponent == 's' or player == 's' and opponent == 'r':
#         return  
