import hangman_words
import random
import hangman_arts


hangman_word=random.choice(hangman_words.word_list)
hangman_chars = [char for char in hangman_word]
hangman_output_chars=" - " * len(hangman_chars)

# for char in hangman_chars:
print(hangman_output_chars)
print(hangman_word)
print(len(hangman_arts.stages))
