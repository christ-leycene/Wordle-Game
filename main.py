"""This is a python implementation of the Wordle Game.

Based on the online word game created and developed by Welsh software
engineer Josh Wardle. Players have six attempts to guess a five-letter word,
with feedback given for each guess in the form of coloured tiles indicating
when letters match or occupy the correct position.

The current version of this project is for education purposes.

ENSAT 2024/2025.
"""

import os
from sources.display import game_instructions, game_start_display, display_word_feedback, display_win, display_lost
from sources.word_choice import read_words_file, choose_random_word
from sources.validate_guess import get_valid_guess
from sources.wordle import check_guess_correct, feed_back_word, MAX_ATTEMPTS


def main():
    # Read all the words from the file
    words_file_path = os.path.join('assets', 'word.txt')
    all_words = read_words_file(words_file_path)
    
    # Choose a random word from the list
    word_to_guess = choose_random_word(all_words)
    
    # Initialize variables for the game
    attempts = 0
    guesses = []
    
    # Display the game instructions and start message
    game_instructions()
    game_start_display()
    
    # Main game loop
    while attempts < MAX_ATTEMPTS:
        # Get a valid guess from the user
        guess = get_valid_guess(all_words, guesses)
        guesses.append(guess)
        attempts += 1
        
        # Check if the guess is correct
        if check_guess_correct(word_to_guess, guess):
            display_win(word_to_guess, attempts)
            break
        
        # Provide feedback on the guess
        feedback = feed_back_word(word_to_guess, guess)
        display_word_feedback(guess, feedback)
        
    # If the player runs out of attempts, they lose
    if attempts == MAX_ATTEMPTS and not check_guess_correct(word_to_guess, guess):
        display_lost(word_to_guess)


if __name__ == "__main__":
    main()
