import random
import os
import csv

# Create a list of authorized players
authorized_players = ["Player 1", "Player 2"]

# Function to register new players
def register_player():
    new_player = input("Enter the new player's name to register: ")
    if new_player not in authorized_players:
        authorized_players.append(new_player)
        print(f"{new_player} has been registered successfully.")
    else:
        print(f"{new_player} is already registered.")
    return authorized_players

# Function to get player names and check authorization
def get_players():
    print("Authorized players:", ", ".join(authorized_players))
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

        print(f"{player1}: {player1_die} points")
        print(f"{player2}: {player2_die} points")
        print(f"{player1}'s total score: {scores[player1]}")
        print(f"{player2}'s total score: {scores[player2]}\n")
    return scores

# Function to determine winner and save scores
def save_and_display_winner(scores):
    winner = max(scores, key=lambda player: scores[player])
    print(f"The winner is {winner} with a score of {scores[winner]}!")

    with open("top_scores.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([winner, scores[winner]])

    display_top_scores()

# Function to display top scores
def display_top_scores():
    if os.path.exists("top_scores.csv"):
        with open("top_scores.csv", "r") as file:
            reader = csv.reader(file)
            top_scores = sorted(reader, key=lambda row: int(row[1]), reverse=True)[:5]
            print("Top 5 winning scores:")
            for score in top_scores:
                print(f"{score[0]}: {score[1]}")

# Function to display score history
def display_score_history():
    if os.path.exists("top_scores.csv"):
        with open("top_scores.csv", "r") as file:
            reader = csv.reader(file)
            print("Score History:")
            for row in reader:
                print(f"{row[0]}: {row[1]} points")

# Function to set game settings
def set_game_settings():
    num_rounds = int(input("Enter the number of rounds to play: "))
    return num_rounds

# Main game loop
def main():
    while True:
        action = input("Enter 'play' to play, 'register' to register a new player, 'history' to view score history, 'quit' to quit: ").lower()
        if action == 'play':
            player1, player2 = get_players()
            scores = {player1: 0, player2: 0}
            num_rounds = set_game_settings()

            for round in range(num_rounds):
                player1_score, player2_score = play_round(player1, player2)
                scores = update_scores(player1, player2, scores, player1_score, player2_score)
                display_scores(round, player1, player2, player1_score, player2_score, scores)

            scores = tie_breaker(player1, player2, scores)
            save_and_display_winner(scores)

            if input("Do you want to play again? (yes/no) ").lower() != "yes":
                break
        elif action == 'register':
            register_player()
        elif action == 'history':
            display_score_history()
        elif action == 'quit':
            break
        else:
            print("Invalid action. Please try again.")

# Function to save player profiles
def save_player_profiles():
    with open("player_profiles.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for player in authorized_players:
            writer.writerow([player])
    print("Player profiles saved successfully.")

# Function to load player profiles
def load_player_profiles():
    if os.path.exists("player_profiles.csv"):
        with open("player_profiles.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] not in authorized_players:
                    authorized_players.append(row[0])
        print("Player profiles loaded successfully.")
    else:
        print("No player profiles found. Starting with default players.")

# Function to play a bonus round
def play_bonus_round(player1, player2, scores):
    print("Bonus round!")
    player1_bonus = random.randint(1, 10)
    player2_bonus = random.randint(1, 10)
    scores[player1] += player1_bonus
    scores[player2] += player2_bonus
    print(f"{player1} earned {player1_bonus} bonus points.")
    print(f"{player2} earned {player2_bonus} bonus points.")
    return scores

# Function to handle invalid input
def get_valid_input(prompt, valid_options):
    while True:
        response = input(prompt).lower()
        if response in valid_options:
            return response
        else:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

# Function to manage player profiles
def manage_profiles():
    while True:
        action = get_valid_input("Enter 'view' to view profiles, 'add' to add a profile, 'remove' to remove a profile, 'back' to go back: ", ['view', 'add', 'remove', 'back'])
        if action == 'view':
            print("Authorized players:", ", ".join(authorized_players))
        elif action == 'add':
            register_player()
        elif action == 'remove':
            player_to_remove = input("Enter the name of the player to remove: ")
            if player_to_remove in authorized_players:
                authorized_players.remove(player_to_remove)
                print(f"{player_to_remove} has been removed.")
            else:
                print("Player not found.")
        elif action == 'back':
            break

# Enhanced main game loop
def main():
    load_player_profiles()
    while True:
        action = get_valid_input("Enter 'play' to play, 'profiles' to manage profiles, 'history' to view score history, 'quit' to quit: ", ['play', 'profiles', 'history', 'quit'])
        if action == 'play':
            player1, player2 = get_players()
            scores = {player1: 0, player2: 0}
            num_rounds = set_game_settings()

            for round in range(num_rounds):
                player1_score, player2_score = play_round(player1, player2)
                scores = update_scores(player1, player2, scores, player1_score, player2_score)
                display_scores(round, player1, player2, player1_score, player2_score, scores)
                
                if round == num_rounds - 1:
                    scores = play_bonus_round(player1, player2, scores)

            scores = tie_breaker(player1, player2, scores)
            save_and_display_winner(scores)

            if get_valid_input("Do you want to play again? (yes/no) ", ['yes', 'no']) != "yes":
                break
        elif action == 'profiles':
            manage_profiles()
        elif action == 'history':
            display_score_history()
        elif action == 'quit':
            save_player_profiles()
            break



if __name__ == "__main__":
    main()
