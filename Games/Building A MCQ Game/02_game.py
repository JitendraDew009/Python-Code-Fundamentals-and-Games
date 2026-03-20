import random

def save_score(name, attempts):
    with open("scores.txt", "a") as file:
        file.write(f"{name},{attempts}\n")

def show_leaderboard():
    try:
        with open("scores.txt", "r") as file:
            scores = []
            for line in file:
                name, attempts = line.strip().split(",")
                scores.append((name, int(attempts)))

            scores.sort(key=lambda x: x[1])

            print("\n Leaderboard (Top 5):")
            for i, (name, attempts) in enumerate(scores[:5], start=1):
                print(f"{i}. {name} - {attempts} attempts")

    except FileNotFoundError:
        print("\nNo scores yet!")

def guessing_game():
    name = input("Enter your name: ")

    level = input("Choose difficulty (easy/medium/hard): ").lower()

    if level == "easy":
        number = random.randint(1, 10)
    elif level == "medium":
        number = random.randint(1, 50)
    else:
        number = random.randint(1, 100)

    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print(f"Correct! You took {attempts} attempts.")
            save_score(name, attempts)
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

    show_leaderboard()

guessing_game()