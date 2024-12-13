import random

def main():
    words = ['hello', 'campus', 'mathematik', 'python', 'weihnachten', 'joanneum',
    'softwaredesign', 'mojiverse', 'designpattern', 'bitcoin']

    word = random.choice(words)
    startMessage = print(f"Welcome to hangman. Your word will be: \n")

    guessedWord, tries = play(word)

    # Success Message with the results.
    print(f"Congratulation. You guessed '{guessedWord}' correctly after {tries} tries")


def play(word):
    # Counter for tried guess.
    tries = 0

    # Create a list of dots with the length of the word.
    toBeGuessed = ['.' for _ in range(len(word))]

    # Iterate through the Guessing word till there is no dot anymore in the word.
    # The tries will not be handled, so it's unlimited.
    while '.' in toBeGuessed:
        currentGuess = input(f"{' '.join(toBeGuessed)} ")
        toBeGuessed = checkCurrentGuess(word, toBeGuessed, currentGuess)

        tries += 1 # Woow, increment a variable like tries++ is not possible in python :O

    guessedWord = ' '.join(toBeGuessed)
    # Print the final word after guessing is finished
    print(guessedWord)

    return guessedWord, tries

def checkCurrentGuess(word, toBeGuessed, currentGuess):
    for i in range(len(word)):
        if word[i] == currentGuess.lower():
            toBeGuessed[i] = currentGuess

    return toBeGuessed


# Initialize the main function.
main()