import random

def guess(max_num):
    random_number = random.randint(1, max_num)
    guessed_number = int(input(f"I have a number between 1 and {max_num}. What do you think it is? "))
    tries = 1
    while random_number != guessed_number:
        tries += 1
        if guessed_number > random_number:
            guessed_number = int(input("Too high! Try again: "))
        elif guessed_number < random_number:
            guessed_number = int(input("Too low! Try again: "))
        
    print(f"You got it right! It is {guessed_number}. You got it on {tries} attempt/s")

def computer_guess(max_num):
    tries = 0
    low = 1
    is_correct = ''
    random_number = 0
    while is_correct != 'c':
        tries += 1
        random_number = random.randint(low, max_num)
        is_correct = input(f"Computer: Is it {random_number}? Is it low (L), high (H) or Correct (C)? ").lower()
        if is_correct == "h":
            max_num = random_number - 1
        elif is_correct == "l":
            low = random_number + 1
        
    print(f"Yay! It is {random_number}. I guessed it on {tries} attempt/s")

# guess(100)
computer_guess(100)