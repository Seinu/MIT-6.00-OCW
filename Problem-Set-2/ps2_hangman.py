# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def concatenateWord(word):
    c = ''
    for i in range(0, len(word)):
        c = c + word[i]
    return c

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
word = choose_word(wordlist)
# your code begins here!
abc = 'abcdefghijklmnopqrstuvwyxz'
print 'Welcome to the game, Hangman!'
print 'I am thinking of a word that is', len(word), 'letters long.'
print '-------------'
wordGuessed = []
strWordGuessed = ''
for i in range(0, len(word)):
    wordGuessed.append('_ ')
print concatenateWord(wordGuessed)
print strWordGuessed
count = 0
maxGuess = int(len(word) * 1.5)
while count < maxGuess:
    print 'You have', maxGuess - count, 'guesses left.'
    print 'available letters: ', abc
    letterGuessed = raw_input('Please guess a letter: ')
    inWord = False
    if letterGuessed not in abc:
        print 'This letter has already been guessed!', strWordGuessed
    else:
        for x, l in enumerate(word):
            if l == letterGuessed:
                wordGuessed[x] = l
                strWordGuessed = concatenateWord(wordGuessed)
                inWord = True
                
        if inWord == True:        
            print 'Good guess:', strWordGuessed
        else:
            count += 1
            print 'Oops! That letter is not in my word:', strWordGuessed
    abc = abc.replace(letterGuessed, '')
    print '-------------'
    if strWordGuessed == word:
        print 'Congratulations, you won!'
        break