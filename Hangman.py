import random

def choose_word():
    word_bank = ["hangman", "python", "game", "docker"]
    word = random.choice(word_bank)
    return word

def play_game():
    word = choose_word()
    word_progress = ["_" for _ in word]
    num_guesses = 6

    while True:
        print(f"Word: {' '.join(word_progress)}")
        print(f"Guesses remaining: {num_guesses}")

        letter = input("Guess a letter: ")

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_progress[i] = letter

            if "_" not in word_progress:
                print("You won!")
                break
        else:
            num_guesses -= 1

            if num_guesses == 0:
                print("You lost :(")
                break

play_game()
