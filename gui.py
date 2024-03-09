import random
import tkinter as tk
from tkinter import messagebox

def check_rule(ch1, ch2, rules, score):
    if ch1 == ch2:
        return "Tie!!", score
    if rules[ch1] == ch2:
        return "You lost!", 0
    else:
        return "You win!", score + 1

def play_game(user_choice):
    computer_choice = random.choice(options)
    result, score = check_rule(user_choice, computer_choice, rules, int(score_label["text"]))
    score_label.config(text=str(score))
    messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")

def select_rock():
    play_game("rock")

def select_paper():
    play_game("paper")

def select_scissors():
    play_game("scissors")

rules = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
options = ["rock", "paper", "scissors"]

root = tk.Tk()
root.title("Rock Paper Scissors Game")

score_label = tk.Label(root, text="0")
score_label.pack()

rock_button = tk.Button(root, text="Rock", command=select_rock)
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=select_paper)
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=select_scissors)
scissors_button.pack()

root.mainloop()
