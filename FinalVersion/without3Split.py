import random
import statistics

def main():
    # User input for the number of turns
    amount = int(input("Enter the number of turns: "))

    # Initialize counters for card counts and reshuffles
    spaceCounters = [[0, 0, 0, 0] for _ in range(14)]  # Counters for each space and card [space][card]
    emptyCountTotal = 0
    slideUsageCount = 0  # Counter for slide usage
    fourShortcut = 0  # Counter for how often the four shortcut is used

    # Run the game simulation and collect statistics
    totalArr, spaceCounters, emptyCountTotal, slideUsageCount, fourShortcut = miniSorry(amount, spaceCounters)

    # Print game statistics
    print("Game Statistics")
    print("----------------")
    print(f"Average game length: {statistics.mean(totalArr):.3f}")
    print(f"Standard deviation of game length: {statistics.stdev(totalArr):.3f}")
    print(f"Number of times the deck was reshuffled: {emptyCountTotal}")
    print(f"Number of times the slide from space 5 to space 8 was used: {slideUsageCount}")
    print(f"Number of times the spot 2 shotcut was used: {fourShortcut}")
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
    fourShortcut = 0 # Counter for how often the spot 2 shotcut is used

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
            elif ran == 4 and spot == 2:  # Special case: if on spot two when 4 is drawn go to spot 10
                spot = 10
                fourShortcut += 1
            elif ran == 4 and spot >= 10:  # Special case: if 4 is drawn and it sends you over the limit you move back one instead
                spot -= 1
            else:  # Regular case: move to a different space
                spot += ran

            if spot > 13:
                spot -= ran  # Adjust the spot if it exceeds 13 (end space)
            deck.remove(ran)  # Remove the drawn card from the deck

            if not deck:  # Check if the deck is empty
                deck = deckOriginal[:]  # Reshuffle the deck by restoring the original deck
                emptyCount += 1

            turns += 1  # Increment the turn count

        totalArr.append(turns)  # Store the game length

    return totalArr, spaceCounters, emptyCount, slideUsageCount, fourShortcut


if __name__ == '__main__':
    main()
