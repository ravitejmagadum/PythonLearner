import random
word_list = ["aardvark", "babaoon", "camael"]
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

# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
choosen_word = random.choice(word_list)



# for letter in choosen_word:
#   if guess == letter:
#     print("right")
#   else:
#     print("wrong")
list1 = []
s = len(choosen_word)

for n in range(0, s):
  list1.append("_")
print(list1)
# guess = input("guess a letter\n").lower()
list2 = list1
lives = 0
hangman = True

while "_" in list2:
   
  guess = input("guess a letter\n").lower()
  
  for position in range(s):  
    if choosen_word[position] == guess:
      list2[position] = guess 
  print(list2)
  if guess not in choosen_word:
      if lives < 6:
        lives += 1
        print(f"You lost {lives} life")
        print(stages[lives-1])
      else: 
        hangman = False
        print("You lost the game")
        print(stages[-1])
        break
else:  
  print("You Win ")
