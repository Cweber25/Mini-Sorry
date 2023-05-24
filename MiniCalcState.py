# Cole Weber
# Mini Sorry Problem
# 3/21/2023
# Problem Definition: The game consists of a board that is 14 spaces long. The first space is START, the last is HOME,
# and in between are labelled 1 through 12. There is a deck of 13 cards which includes four 1s
# and 3 each of 2,3,4. The player’s token starts at the START space and a card is drawn from the
# shuffled deck. The token moves that many spaces toward HOME. Play continues drawing a card
# and moving forward. However, the token must reach the HOME space by exact count, so if a
# card is drawn that would move the token beyond HOME, then the token does not move. The
# deck of cards is not drawn between draws, but if all 13 cards are used then the deck is shuffled
# and play continues.

import random
import statistics

# Call the game function to get the average amount of turns it takes to get to the home space.


def main():
#    amount = int(input("Enter amount of turns: "))
   totalArr = []
   oneTotal = []
   twoTotal = []
   threeTotal = []
   fourTotal = []
   oneA = []
   twoA = []
   threeA = []
   fourA = []
   emptyCountTotal = 0
   # Amount is the amount of games it takes to get to the home space. Change it to calculate any amount you want.
   stateArray,emptyCountTotal,oneTotal,twoTotal,threeTotal,fourTotal,totalArr = miniSorry()

   print(" The mean amount of turns is", statistics.mean(totalArr))
   print(" The standard deviation amount of turns is", statistics.stdev(totalArr))

   print(" These are the amount of times these numbers are drawn \n1: ", sum(oneTotal),"2: ", sum(twoTotal),"3: ", sum(threeTotal),"4: ", sum(fourTotal),"\n")


   
   for states in range(14):
        for num in stateArray[states]:
                if num == 1:
                    oneA.append(num)
                if num == 2:
                    twoA.append(num)
                if num == 3:
                    threeA.append(num)
                if num == 4:
                    fourA.append(num)
        print(states, "1 :", len(oneA),"|2 :",len(twoA),"|3 :",len(threeA),"|4 :",len(fourA),"\n")
        oneA = []
        twoA = []
        threeA = []
        fourA = []
   print("The deck got shuffled", emptyCountTotal, "time(s)\n" )

   
        
   

   

    

def miniSorry():
 
    amount = int(input("Enter amount of turns: "))
    totalArr = [] * amount
    oneTotal = []
    twoTotal = []
    threeTotal = []
    fourTotal = []
    
    StateArray = [[], [], [], [],[],[],[],[],[],[],[],[],[],[]]
    emptyCount = 0
    for a in range(amount):
        turns = 0
        spot = 0
        deck = [1,1,1,1,2,2,2,3,3,3,4,4,4]
        deckOriginal = [1,1,1,1,2,2,2,3,3,3,4,4,4]
        
        # This loops through the code to check to see what spot the piece is at
        while(spot != 13):
            # Chooses a random card from the deck and moves the piece
            ran = random.choice (deck)
            StateArray[spot].append(ran)
            spot += ran
            if ran == 1:
                oneTotal.append(1)
            if ran == 2:
                twoTotal.append(1)
            if ran == 3:
                threeTotal.append(1)
            if ran == 4:
                fourTotal.append(1)

            
            # If the number were to move past home then it returns to previous location and removes card from deck
            if spot > 13:
                spot = spot - ran
            deck.remove(ran)
            
            # If the deck is empty it refills the deck
            if not deck:
                deck = deckOriginal[:]
                emptyCount = emptyCount + 1
            # Counts the amount of turns and returns them at end of program

            
            
            turns += 1
        totalArr.append(turns)
        

    
    return StateArray,emptyCount,oneTotal,twoTotal,threeTotal,fourTotal,totalArr
            
    

if __name__ == '__main__':
    main()