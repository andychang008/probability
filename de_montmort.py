import random
import math_methods

n = int(input("Enter the size of the deck for which you will draw from: ")) #number of total cards
t = int(input("Enter how many times you would like to run this probability simulation: ")) #number of simulations ran
cards = list(range(1,n+1))
match = False
win_counter = 0
win_prob = 0

for i in range(1,n+1):
    win_prob = win_prob + (((-1) ** (i+1)) * math_methods.nCr(n,i) * math_methods.factorials(n-i)) / math_methods.factorials(n)

def play(cards, t):
    win_counter = 0
    for i in range(t):
        random.shuffle(cards)
        for i in range(0,n):
            if i+1 == cards[i]:
                match = True
                win_counter = win_counter + 1
                break
    win_rate = win_counter / t
    print("Out of " + str(t) + " times that you played, with a deck of " + str(n) + " cards, you have won " + str(win_counter) + " times! That is a win rate of " + str(win_rate) + "!")
    print("Compared to the expected probability of " + str(win_prob) + " your win rate deviates by " + str((win_rate-win_prob)/win_prob * 100) + "%!")
play(cards, t)


