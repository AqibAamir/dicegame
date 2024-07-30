import random
import os
import csv

# Create a list of authorized players
authorized_players = ["Player 1", "Player 2"]

# Function to get player names and check authorization
def get_players():
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")
    if player1 not in authorized_players or player2 not in authorized_players:
        print("Unauthorized player. Please try again.")
        exit()
    return player1, player2

# Function to play a single round of the game
def play_round(player1, player2):
    player1_dice1 = random.randint(1, 6)
    player1_dice2 = random.randint(1, 6)
    player2_dice1 = random.randint(1, 6)
    player2_dice2 = random.randint(1, 6)

    player1_score = player1_dice1 + player1_dice2
    player2_score = player2_dice1 + player2_dice2

    if player1_score % 2 == 0:
        player1_score += 10
    else:
        player1_score -= 5
    if player2_score % 2 == 0:
        player2_score += 10
    else:
        player2_score -= 5

    if player1_dice1 == player1_dice2:
        player1_score += random.randint(1, 6)
    if player2_dice1 == player2_dice2:
        player2_score += random.randint(1, 6)

    return player1_score, player2_score

# Function to update scores
def update_scores(player1, player2, scores, player1_score, player2_score):
    scores[player1] += player1_score
    scores[player2] += player2_score
    return scores

# Function to display scores
def display_scores(round, player1, player2, player1_score, player2_score, scores):
    print(f"Round {round + 1} scores:")
    print(f"{player1}: {player1_score} points")
    print(f"{player2}: {player2_score} points")
    print(f"{player1}'s total score: {scores[player1]}")
    print(f"{player2}'s total score: {scores[player2]}\n")

# Function to handle tie-breaker
def tie_breaker(player1, player2, scores):
    while scores[player1] == scores[player2]:
        player1_die = random.randint(1, 6)
        player2_die = random.randint(1, 6)

        scores[player1] += player1_die
        scores[player2] += player2_die


