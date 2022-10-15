import random

def play():
    user_hand = input("What's your choice?\n'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer_hand = random.choice(['r', 'p', 's'])
    
    if user_hand == computer_hand:
        return "It's a tie"
    
    if is_win(user_hand, computer_hand):
        return "You won!"
    
    return "You lost!"
        
def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True
    return False


print(play())