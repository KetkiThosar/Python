# Python program to shuffle deck of card using the module random and draw 5 cards

import itertools,random


#make a deck of the cards
deck=list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

#shuffle the cards
random.shuffle(deck)

print('You got')

for i in range(5):
    print(deck[i][0]," of ",deck[i][1])

