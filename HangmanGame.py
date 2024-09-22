import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

placeholder = "_" * word_length
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word! You lose a life!")

    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if lives == 0:
        game_over = True
        print(f"******************It was '{chosen_word}', YOU LOSE**********************")
    elif "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
