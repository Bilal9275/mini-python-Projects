import random

easy_words = ['apple', 'ball', 'cat', 'dog', 'egg', 'fish', 'hat', 'ice', 'jam', 'kite']
medium_words = ['banana', 'guitar', 'python', 'jumble', 'flower', 'window', 'puzzle', 'rocket', 'silver', 'turtle']
hard_words = ['xylophone', 'quizzical', 'pneumonia', 'juxtapose', 'mnemonic', 'zephyr', 'whimsical', 'labyrinth', 'cryptic', 'vortex']

print("Welcome to the Word Guessing Game!")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter difficulty level: ").lower()

if level == "easy":
    word_list = random.choice(easy_words)
elif level == "medium":
    word_list = random.choice(medium_words)
elif level == "hard":
    word_list = random.choice(hard_words)
else:
    print("Invalid level. Defaulting to easy.")
    word_list = random.choice(easy_words)

attempts = 0
print("\nGuess the word:")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == word_list:
        print(f"Congratulations! You've guessed the word '{word_list}' in {attempts} attempts.")
        break
    else:
        print("Incorrect guess. Try again!")

    hint = ""
    for i in range(len(word_list)):
        if i < len(guess) and guess[i] == word_list[i]:
            hint += guess[i]
        else:
            hint += "_"
    print(f"Hint: {hint}")
print("Thank you for playing!")