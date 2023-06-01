import random
import statistics

def main():
    # User input for the number of turns
    amount = int(input("Enter the number of turns: "))

    # Initialize counters for card counts and reshuffles
    spaceCounters = [[0, 0, 0, 0] for _ in range(14)]  # Counters for each space and card [space][card]
    emptyCountTotal = 0
    slideUsageCount = 0  # Counter for slide usage
    splitToSlideCount = 0  # Counter for how often the 3 card is split to use the slide
    splitToSpace13Count = 0  # Counter for how often the 3 card is split to reach space 13

    # Run the game simulation and collect statistics
    totalArr, spaceCounters, emptyCountTotal, slideUsageCount, splitToSlideCount, splitToSpace13Count = miniSorry(amount, spaceCounters)

    # Print game statistics
    print("Game Statistics")
    print("----------------")
    print(f"Average game length: {statistics.mean(totalArr):.3f}")
    print(f"Standard deviation of game length: {statistics.stdev(totalArr):.3f}")
    print(f"Number of times the deck was reshuffled: {emptyCountTotal}")
    print(f"Number of times the slide from space 5 to space 8 was used: {slideUsageCount}")
    print(f"Number of times the 3 card was split to use the slide: {splitToSlideCount}")
    print(f"Number of times the 3 card was split to reach space 13: {splitToSpace13Count}")
    print("\nCard counts and proportions for each card at each space:")
    print("--------------------------------------------------------")

    # Print card counts and proportions for each space
    for space, counters in enumerate(spaceCounters):
        total = sum(counters)
        proportions = [count / total if total != 0 else 0 for count in counters]
        print(f"Space {space}:")
        print(f"  Card Counts - 1: {counters[0]}, 2: {counters[1]}, 3: {counters[2]}, 4: {counters[3]}")
        print(f"  Proportions - 1: {proportions[0]:.4f}, 2: {proportions[1]:.4f}, 3: {proportions[2]:.4f}, 4: {proportions[3]:.4f}")
        print()

    print(f"The deck was reshuffled {emptyCountTotal} time(s).\n")


def miniSorry(amount, spaceCounters):
    totalArr = []  # List to store game lengths
    emptyCount = 0  # Counter for deck reshuffles
    slideUsageCount = 0  # Counter for slide usage
    splitToSlideCount = 0  # Counter for how often the 3 card is split to use the slide
    splitToSpace13Count = 0  # Counter for how often the 3 card is split to reach space 13

    for _ in range(amount):
        turns = 0
        spot = 0
        deck = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]  # Initial deck of cards
        deckOriginal = deck[:]  # Make a copy of the original deck

        while spot != 13:
            ran = random.choice(deck)  # Draw a card randomly from the deck
            spaceCounters[spot][ran - 1] += 1  # Increment the counter for the card at the current space

            if spot + ran == 5:  # Special case: slide from space 5 to space 8
                spot = 8
                slideUsageCount += 1
            elif ran == 3 and spot + ran <= 13:  # Special case: split the 3 card
                if spot + ran == 5:  # Split to use the slide
                    spot = 5  # Move to space 5
                    spot += 3 - (5 - spot)  # Move remaining distance after hitting space 5
                    slideUsageCount += 1
                    splitToSlideCount += 1
                elif spot + ran == 13:  # Split to reach space 13
                    spot = 13
                    splitToSpace13Count += 1
                else:  # Split to reach any other space
                    remaining = 13 - spot
                    splitMoves = [1, 2]
                    if remaining < 2:
                        splitMoves = [remaining]
                    elif remaining < 3:
                        splitMoves = [2, remaining - 2]
                    spot += sum(splitMoves)
            else:
                spot += ran

            if spot > 13:
                spot -= ran  # Adjust the spot if it exceeds 13 (end space)
            deck.remove(ran)  # Remove the drawn card from the deck

            if not deck:  # Check if the deck is empty
                deck = deckOriginal[:]  # Reshuffle the deck by restoring the original deck
                emptyCount += 1

            turns += 1  # Increment the turn count

        totalArr.append(turns)  # Store the game length

    return totalArr, spaceCounters, emptyCount, slideUsageCount, splitToSlideCount, splitToSpace13Count


if __name__ == '__main__':
    main()
