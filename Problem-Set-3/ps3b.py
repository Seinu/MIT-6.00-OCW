from ps3a import *
import time
from perm import *


n = 0
#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    words = []
    for i in range(1, len(hand)):
        x = get_perms(hand, i)
        words.extend(x)
    
    score = 0
    maxscore = 0
    bestword = ''
    
    for word in words:
        if word in word_list:
            score = get_word_score(word, len(hand))
            if score > maxscore:
                bestword = word
                maxscore = score
    if maxscore == 0:
        return
                
    return bestword
            
    
    

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    
    word = ''
    score = 0
    while word != None:
        print display_hand(hand)
        word = comp_choose_word(hand, word_list)
        if is_valid_word(word,hand,word_list):
            print word
            hand = update_hand(hand, word)
            score = score + get_word_score(word, n)
        print score
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    
    opt = ''
    opt2 = ''
    while opt != 'e':
        opt = raw_input('input e to exit, n for new hand, r to replay hand: ')
        opt2 = raw_input("Input u to play as user, input c for cpu to play. ")
        if opt == 'n':
            n = int(raw_input('input hand size. '))
            if opt2 == 'u':
                hand = deal_hand(n)
                play_hand(hand, word_list)
            elif opt2 == 'c':
                hand = deal_hand(n)
                comp_play_hand(hand, word_list)
        elif opt == 'r':
            if opt2 == 'u':
                play_hand(hand, word_list)
            elif opt2 == 'c':
                comp_play_hand(hand, word_list)
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
