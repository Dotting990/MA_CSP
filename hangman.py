# MA, Hangman
import random

guess = 6

with open("wlist.txt", "r") as file:
    words = file.read().split(",")
answer = random.choice(words)
"""______
   |     |
   |     O
   |    /|\\
   |    /\\
   |_________"""
for answer in range (1, answer+1):
    letter = input("Welcome to Hangman, you are given ")