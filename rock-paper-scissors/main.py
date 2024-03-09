import random


def check_rule(ch1, ch2, rules, score):
    if(ch1 == ch2):
        print("Tie!!")
        return 1, score
    if(rules[ch1] == ch2):
         #if ch2 defeats ch1 -- computer defeats user
        print("You lost!")
        return 0, 0
    else:
        print("You win")
        # print(f"\nYour current score is {score}")
        return 1, score + 1
    

rules = {"rock" : "paper", "paper" : "scissors", "scissors" : "rock"}  #value defeats key
options = ["rock", "paper", "scissors"]

score = 0

# print("\n")

while True:
    computer_choice = random.choice(options)
    user_choice = input("Enter rock, paper or scissors: ")
    if(user_choice not in options):
        print("Invalid entry! Please enter one")
    else:
        print("Computer chose ", computer_choice)
        valid, score = check_rule(user_choice, computer_choice, rules, score)
        print(f"\nYour current score is {score}")
        
    if(valid == 0): 
        break



