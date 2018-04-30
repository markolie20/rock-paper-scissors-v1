import random

options = ["scissors", "paper", "rock"]

i = random.randint(0, (len(options) - 1))

playedHand = input("PLay rock, paper or scissors please: ")

computerPlayedHand = options[i]

if playedHand == "rock" and computerPlayedHand == "scissors":
    print("the computer had scissors, you win")
elif playedHand == "rock" and computerPlayedHand == "paper":
    print("the computer had paper, you lose")
elif playedHand == "rock" and computerPlayedHand == "rock":
    print("the computer also had rock, its a tie")
elif playedHand == "paper" and computerPlayedHand == "rock":
    print("the computer had rock, you win")
elif playedHand == "paper" and computerPlayedHand == "scissors":
    print("the computer had scissors, you lose")
elif playedHand == "paper" and computerPlayedHand == "paper":
    print("the computer also had paper, its a tie")
elif playedHand == "scissors" and computerPlayedHand == "paper":
    print("the computer had paper, you win")
elif playedHand == "scissors" and computerPlayedHand == "scissors":
    print("the computer also had scissors, its a tie")
elif playedHand == "scissors" and computerPlayedHand == "rock":
    print("the computer had rock, you lose")
else:
    print("please only state rock, paper or scissors")

