import subprocess
import platform

def open_app(Among Us):
    system_platform = platform.system()

    try:
        if system_platform == "Darwin":  # macOS
            subprocess.run(["open", "-a", Among_Us])
        elif system_platform == "Windows":  # Windows
            subprocess.run(["start", "", Among_Us], shell=True)
        elif system_platform == "Linux":  # Linux
            subprocess.run([Among_Us])
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    app_to_open = input("Enter the name of the app to open: ")
    open_app(app_to_open)

import random

# List of players
players = ["PenguinFsih", "PooPooHead", "megongaga", "BarnieTheDinasaur", "PeppaPig"]

# AI's strategy
def ai_strategy():
    suspicious_player = random.choice(players)
    return suspicious_player

# Simulate the game
def play_among_us():
    imposter = random.choice(players)
    print(f"Among Us: An imposter is among us! It's {imposter}.")

    ai_player = random.choice(players)
    print(f"{ai_player} is an AI.")

    while len(players) > 2:
        # AI's turn to vote
        vote_target = ai_strategy()
        print(f"{ai_player} votes for {vote_target}.")

        # Player elimination
        if vote_target == imposter:
            print(f"{vote_target} was an imposter! {ai_player} wins!")
            break
        else:
            print(f"{vote_target} was not an imposter.")
            players.remove(vote_target)
            if len(players) == 2:
                print(f"The remaining players are: {', '.join(players)}.")
                print("The imposter wins!")
                break

if __name__ == "__main__":
    play_among_us()
