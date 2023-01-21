import random
from module_for_7 import word_list
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
chosen_word = random.choice(word_list)
end_of_game = False
lives = len(stages)
display = []
for letter in chosen_word:
    # for x in range(len(chosen_word))
    display += "_"

no_of_guess = 0
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
       letter = chosen_word[position]
       if letter == guess:
          display[position] = letter
          print(display)

    if "_" not in display:
        end_of_game = True
        print("\nYOU WON")

    if guess not in chosen_word:
        print(f"You guessed {guess}, which is not in this word, you loose a life!")
        print(display)
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYOU LOOSE")
        print(stages[lives])

