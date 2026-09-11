#TASK: Get the score for each user and declare the winner
#paly the game for 10 times -->(push in github and share it (tasks folder in git)
#Task 2 -->Give user a choice -->RPS(1) /NG (number gusseing ) (2)/3 (Study) /any number
#no choice only 1,2,3 -->Function

#Rock paper scissiors

import random,time

# Playing a game (Rock Paper Scissors)

player1_score = 0
player2_score = 0

for i in range(10):

    print("\nGame", i + 1)

    player1 = input("Enter one of these --> Rock, Paper, Scissors: ").lower().strip()

    player2 = random.choice(['rock', 'paper', 'scissors'])

    print("Player 2:", player2)

    if player1 == "rock" and player2 == "paper":
        print("Player2 Won...")
        player2_score += 1

    elif player1 == "paper" and player2 == "scissors":
        print("Player2 Won...")
        player2_score += 1

    elif player1 == "scissors" and player2 == "rock":
        print("Player2 Won...")
        player2_score += 1

    elif player1 == player2:
        print("Tie!")

    else:
        print("Player1 Won...")
        player1_score += 1


print("\n----- FINAL SCORE -----")
print("Player1 Score:", player1_score)
print("Player2 Score:", player2_score)

if player1_score > player2_score:
    print("Player1 is the Winner!")

elif player2_score > player1_score:
    print("Player2 is the Winner!")

else:
    print("Match Tie!")
