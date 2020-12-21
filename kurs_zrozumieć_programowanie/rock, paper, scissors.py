import random
player_points = 0
computer_points = 0
list = ["rock", "paper", "scissors"]
while player_points < 3 and computer_points < 3:
    player = input("rock/paper/scissors?: ")
    computer = random.choice(list)
    print("players:", player, "vs", "computers:", computer)
    if player == "rock":
        if computer == "paper":
            computer_points += 1
        if computer == "scissors":
            player_points += 1
    if player == "paper":
        if computer == "rock":
            player_points += 1
        if computer == "scissors":
            computer_points += 1
    if player == "scissors":
        if computer == "rock":
            computer_points += 1
        if computer == "paper":
            player_points += 1

    print("player:", player_points, ", computer:", computer_points)
print("Dzięki za grę!")


