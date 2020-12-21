import random

# licznik punktów
player_points = 0
computer_points = 0

list_of_posible_computer_choice = ["rock", "paper", "scissors"]

print("Witam Cię w grze rock/paper/scissors! Zasady są następujące")
print("Musisz wpisać jedną z trzech opcji: rock/paper/scissors")
print("Po twoim wyborze zostanie rozegrana runda.")
print("Na koniec każdej rundy zostanie podanu wynik obu graczy (twój i komputera")
print("Gramy do trzech wygranych rund. Jeśli któryś z graczy osiągnie ten wynik, gra się zakończy i zostanie podany zwycięzca")
print("Dobrej zabawy :)\n")
while player_points < 3 and computer_points < 3:
    player = input("rock/paper/scissors?: ")
    if player != "rock" and player != "paper" and player != "scissors":
        print("oj. Musiałeś coś źle wpisać, Spróbuj raz jeszcze wpisać jedno z następujących:\n rock, paper lub scissors")
        continue
    computer = random.choice(list_of_posible_computer_choice)
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



if player_points > computer_points:
    print("\nGratuluje, wygrałeś!")
else:
    print("\nNiestety ale tym razem wygrał komputer...")
print("Dzięki za grę!")

