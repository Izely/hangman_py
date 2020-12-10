import random

#list of words from which secret word is to be chosen
words = ['tracy', 'annastacia', 'brenda', 'yvone', 'amos', 'alia', 'gretchen', 'annabelle', 'annalese', 'uriel']
word = '----------------'
hang = True   

def choose():
    '''selects a random word, from the words list, to be guessed'''
    random_word = words[random.randint(0,len(words))]
    print('The word has ', len(random_word),' letters')
    return random_word

def position():
    '''finds all the positions, in the secret word, the guessed letter is found'''
    indexes = [pos + 1 for pos in range(len(chosen)) if chosen[pos] == guess]
    return indexes
    
chosen = choose() # selecting the secret word

#loop to give the player 10 chances to dodge the norse
for chances in range(10):
    if word == '-' + chosen:       # if you win
        print('You get to WALK AWAY from the gibbet. *__*')
        hang = False
        break
    guess = input('guess a letter you think is in the word :')
    
    def word_status():
         '''visual status of progress
         shows correctly guessed letters in their correct position(s) in the secret word'''
         global word
         temp = list(word)
         del temp[len(chosen) + 1:]
         for each in position(): temp[each] = guess
         word = ''.join(temp)
         print(word)
	 #word = (each for each in chosen if each == guess else '-')
	 #print(each for each in chosen if each == guess else '-') # this is as good as using word

    if guess in chosen:
        print('"{}" is the {}th letter in the word'.format(guess, position()))
        word_status()
    else:
        print(guess,' is not a letter in the word')

if hang == True:       # if you get to hang
    print('   WELL! There"s the chance of an afterlife ? -_-')



