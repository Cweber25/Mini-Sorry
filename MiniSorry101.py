# Cole Weber
# Mini Sorry Problem
# 5/17/2023
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

def main():
    # User input for the number of turns
    amount = int(input("Enter the number of turns: "))

    # Initialize counters for card counts and reshuffles
    spaceCounters = [[0, 0, 0, 0] for _ in range(14)]  # Counters for each space and card [space][card]
    emptyCountTotal = 0

    # Run the game simulation and collect statistics
    totalArr, spaceCounters, emptyCountTotal = miniSorry(amount, spaceCounters)

    # Print game statistics
    print("Game Statistics")
    print("----------------")
    print(f"Average game length: {statistics.mean(totalArr):.3f}")
    print(f"Standard deviation of game length: {statistics.stdev(totalArr):.3f}")
    print(f"Number of times the deck was reshuffled: {emptyCountTotal}")
    print("\nCard counts and proportions for each card at each space:")
    print("--------------------------------------------------------")

    # Print card counts and proportions for each space
    for space, counters in enumerate(spaceCounters):
        total = sum(counters)
        proportions = [count / total if total != 0 else 0 for count in counters]
        print(f"Space {space}:")
        print(f"  Card Counts - 1: {counters[0]}, 2: {counters[1]}, 3: {counters[2]}, 4: {counters[3]}")
        print(f"  Proportions - 1: {proportions[0]:.2f}, 2: {proportions[1]:.2f}, 3: {proportions[2]:.2f}, 4: {proportions[3]:.2f}")
        print()

    print(f"The deck was reshuffled {emptyCountTotal} time(s).\n")


def miniSorry(amount, spaceCounters):
    totalArr = []  # List to store game lengths
    emptyCount = 0  # Counter for deck reshuffles

    for _ in range(amount):
        turns = 0
        spot = 0
        deck = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]  # Initial deck of cards
        deckOriginal = deck[:]  # Make a copy of the original deck

        while spot != 13:
            ran = random.choice(deck)  # Draw a card randomly from the deck
            spaceCounters[spot][ran - 1] += 1  # Increment the counter for the card at the current space
            spot += ran

            if spot > 13:
                spot -= ran  # Adjust the spot if it exceeds 13 (end space)
            deck.remove(ran)  # Remove the drawn card from the deck

            if not deck:  # Check if the deck is empty
                deck = deckOriginal[:]  # Reshuffle the deck by restoring the original deck
                emptyCount += 1

            turns += 1  # Increment the turn count

        totalArr.append(turns)  # Store the game length

    return totalArr, spaceCounters, emptyCount


if __name__ == '__main__':
    main()
