import random

# List of 5 predefined words
words = ["python", "computer", "program", "science", "coding"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while incorrect_guesses > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Incorrect guesses left:", incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        incorrect_guesses -= 1
        print("Wrong guess!")

# Final result
if "_" not in guessed_word:
    print("\nCongratulations! 🎉")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)