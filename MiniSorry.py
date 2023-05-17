# Cole Weber
# Mini Sorry Problem

import random

def main(): 
    turns = 0
    spot = 0
    deck = [1,1,1,1,2,2,2,3,3,3,4,4,4]
    deckOriginal = [1,1,1,1,2,2,2,3,3,3,4,4,4]
    one,two,three,four = 0,0,0,0

    while(spot != 13):
        ran = random.choice (deck)
        spot += ran
        if ran == 1:
            one += one + 1
        elif ran == 2:
            two += two + 1
        elif ran == 3:
            three += two + 1
        elif ran == 4:
            four += four + 1
        if spot > 13:
            spot = spot - ran
        deck.remove(ran)
        print(deck, ran)
        print("The spot you are at is ", spot)
        
        if not deck:
            deck = deckOriginal[:]
        turns += 1
    print("Game won. It went through ",turns, "  turns")
    print("1: ", one,"2: ", two,"3: ", three,"4: ", four)

if __name__ == '__main__':
    main()