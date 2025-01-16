import requests
import random


def get_random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    word = response.json()[0]
    return word.lower()


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def print_hangman(incorrect_guesses):
    stages = [
        """
           ------
           |    |
                |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        """
    ]
    print(stages[incorrect_guesses])


def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("\n" * 50)  # Clear the screen to hide the word
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        print_hangman(incorrect_guesses)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print("Incorrect guess!")

        print(display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        if all(letter in guessed_letters for letter in word):
            print_hangman(incorrect_guesses)
            print("Congratulations, you guessed the word!")
            break
    else:
        print_hangman(incorrect_guesses)
        print(f"Sorry, you've run out of guesses. The word was '{word}'.")


if __name__ == "__main__":
    play_hangman()
