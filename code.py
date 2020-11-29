import random
words = ['tracy', 'annastacia', 'brenda', 'yvone', 'amos', 'alia', 'gretchen', 'annabelle', 'annalese', 'uriel']

def choose():
    random_word = words[random.randint(0, len(words))]
    print(random_word)

choose()
#apropriate loop to be added :)
guess = input('guess a letter you think is in the word :')
 #   if guess in rando_word:
