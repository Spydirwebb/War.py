"""The card game war as practice
    using:
        dictionaries
        functions
        variables
        loops
        conditoinals"""
#dependencies
import random

#deck dictionary
card_value = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J": 11, "Q": 12, "K":13, "A":14}
suit = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck =[]
for i in range (0,4):
    for char in suit:
        deck.append(char)

#functions
def pile_to_deck(deck, pile):
    random.shuffle(pile)
    deck.clear()
    for i in range(0, len(pile)):
        deck.append(pile[i])
    return deck

#Variables
pick=[]
##play with a suit or the whole deck
while(True):
    choice = input("Pay with a suit(s) or a whole deck(d): ")
    if (choice == 's'):
        pick = pile_to_deck(pick, suit)
        break
    elif(choice == 'd'):
        pick = pile_to_deck(pick, deck)
        break
    else:
        print("Invalid Entry")
my_deck = []
their_deck = []
i=0
random.shuffle(suit)
##split the cards
while (i < len(pick)):
    if(i%2 == 0):
        my_deck.append(pick[i])
    else:
        their_deck.append(pick[i])
    i+=1
my_card = my_deck[0]
their_card = their_deck[0]
my_pile = []
their_pile = []
rounds = 0

#game loop: plays until deck is gone
while (len(my_deck) >0 and len(their_deck) >0):
    #whick is the shorter deck
    short_deck_count = 0
    long_deck_count = 0
    if(len(my_deck)>len(their_deck)):
        short_deck_count = len(their_deck)
        long_deck_count = len(my_deck)
        mine_is_short = False
    else:
        short_deck_count = len(my_deck)
        long_deck_count = len(their_deck)
        mine_is_short = True
    #round loop
    for i in range(0,(short_deck_count)):
        my_card = my_deck[i]
        their_card = their_deck[i]
        print("My Card Number/Value: {}/{}".format(my_card,card_value[str(my_card)]))
        print("Their Card Number/Value: {}/{}".format(their_card, card_value[str(their_card)]))
        #if mine higher
        if(card_value[str(my_card)]> card_value[str(their_card)]):
            print("I win")
            my_pile.append(my_card)
            my_pile.append(their_card)
        #elif equal
        elif(card_value[str(my_card)]== card_value[str(their_card)]):
            print("Tie")
        #else theirs higher
        else:
            print("They Win")
            their_pile.append(my_card)
            their_pile.append(their_card)
    #When someones deck is 0, other person puts remainder of deck into pile
    if(mine_is_short ==False):
        for i in range(short_deck_count, long_deck_count):
            my_pile.append(my_deck[i])
    elif(short_deck_count == long_deck_count):
        pass
    else:
        for i in range(short_deck_count, long_deck_count):
            my_pile.append(their_deck[i])
    #pile to deck, shuffle, empty pile
    print("My Pile: ",my_pile)
    my_deck= pile_to_deck(my_deck, my_pile)
    my_pile.clear()
    print("Their Pile: ",their_pile)
    their_deck = pile_to_deck(their_deck, their_pile)
    their_pile.clear()
    rounds +=1

#win conditionals
if(len(my_deck)>0):
    print("I WON!")
    print("{} Rounds".format(rounds))
else:
    print("they won")
    print("{} Rounds".format(rounds))
