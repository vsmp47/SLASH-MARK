import random
import time

def intro():
    print("May I ask you for your name?")
    name = input("Enter your name: ")
    print(f"{name}, let's play a game. I'm thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Take a guess!")

def pick():
    number = random.randint(1, 200)
    guesses_taken = 0
    while guesses_taken < 6:
        time.sleep(0.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)
            if 1 <= guess <= 200:
                guesses_taken += 1
                if guesses_taken < 6:
                    if guess < number:
                        print("Too low!")
                    elif guess > number:
                        print("Too high!")
                    else:
                        print("Congratulations! You got it!")
                        return True
                else:
                    print("Out of guesses! The number was:", number)
                    return False
            else:
                print("Your guess is out of range. Please enter a number between 1 and 200.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Out of guesses! The number was:", number)
    return False

def main():
    play_again = "yes"
    while play_again.lower() in {"yes", "y"}:
        intro()
        if not pick():
            break
        print("Do you want to play again? (yes/no)")
        play_again = input().lower()

if __name__ == "__main__":
    main()
