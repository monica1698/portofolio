import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(logo)
lives = 6

display = []
word_len = len(chosen_word)
for i in range(len(chosen_word)):
    display += "_"

end_of_game = False

while not end_of_game:
    print("\n")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    guess_letter = input("\nGuess a letter from the word \n").lower() 
    
    if guess_letter in display:
        print(f"You've already guessed {guess_letter} \n")

    for position in range(word_len):
        letter = chosen_word[position]
        if guess_letter == letter:
            display[position] = guess_letter
    if guess_letter not in chosen_word:
        print(f"You've guessed {guess_letter} that is not in the word. You lose a life. \n")
        lives -=1
        if lives == 0:
            end_of_game = True
            print(f"You lose! The word was {chosen_word}.")
    
    if "_" not in display:
        end_of_game = True
        print("You win!")
        
    print(stages[lives])
