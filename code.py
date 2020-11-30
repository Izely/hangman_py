import random

#list of words from which secret word is to be chosen
words = ['tracy', 'annastacia', 'brenda', 'yvone', 'amos', 'alia', 'gretchen', 'annabelle', 'annalese', 'uriel']

def choose():
    '''selects a random word, from the words list, to be guessed'''
    random_word = words[random.randint(0,len(words))]
    print('The word has ', len(random_word),' letters')
    return random_word

def position():
    '''finds all the positions, in the secret word, the guessed letter is found'''
    indexes = [pos + 1 for pos in range(len(chosen)) if chosen[pos] == guess]
    return indexes
    
def word_status():
    '''visual status of progress
     shows correctly guessed letters in their correct position(s) in the secret word'''
    word = '----------------'
    temp = list(word)
    del temp[len(chosen):]
    for each in position(): temp[each] = guess
    word = ''.join(temp)
    print(word)

chosen = choose()   #choosing the secret word

#loop to give the player 10 chances to dodge the norse
for chances in range(10):
    word_status()
    guess = input('guess a letter you think is in the word :')
    if guess in chosen:
        print('{} is a the {} letter in the word'.format(guess, position()))
        word_status()
    else:
        print(guess,' is not a letter in the word')




