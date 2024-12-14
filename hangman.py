import random

def main():
    words = ['hello', 'campus', 'mathematik', 'python', 'weihnachten', 'joanneum',
    'softwaredesign', 'mojiverse', 'designpattern', 'bitcoin']

    scoreboard = {}

    # Using end='' in the print to prevent a newline.
    startMessage = print(f"Welcome to hangman. ", end='')

    # Display the menu for user to choose an option.
    menu(words, scoreboard)

def menu(words, scoreboard):
    tries = 0
    word = random.choice(words)

    # Menu options
    options = input(f"""What will u do?\n
[n]ew game\n
[s]how score\n
[e]nd game\n
> """)

    match options.lower():
        case 'n':
            guessedWord, tries = play(word, tries)

            # Success Message with the results.
            print(f"Congratulation. You guessed '{guessedWord}' correctly after {tries} tries")

            # Update scoreboard for the successfully guessed word.
            scoreboard.update([(word, tries)])

            # remove the guessedWord from the words list.
            words.remove(guessedWord)

            # Reinitialize the word and tries.
            tries = 0
            word = random.choice(words)

            # Call menu function again.
            menu(words, scoreboard)
        case 's':
            print("Your score result's")
            showScoreboard(scoreboard)

            # Call menu function again.
            menu(words, scoreboard)
        case 'e':
            print("Bye Bye")
            exit()
        case _:
            exit()

# Handle the game on new game.
def play(word, tries):
    # Create a list of dots with the length of the word.
    toBeGuessed = ['.' for _ in range(len(word))]

    # Iterate through the Guessing word till there is no dot anymore in the word.
    # The tries will not be handled, so it's unlimited.
    while '.' in toBeGuessed:
        currentGuess = input(f"{' '.join(toBeGuessed)} ")
        toBeGuessed = checkCurrentGuess(word, toBeGuessed, currentGuess)

        tries += 1 # Woow, increment a variable like tries++ is not possible in python :O

    guessedWord = ''.join(toBeGuessed)
    # Print the final word after guessing is finished
    print(guessedWord)

    return guessedWord, tries

# Return the updated guessing word after currentGuess.
def checkCurrentGuess(word, toBeGuessed, currentGuess):
    for i in range(len(word)):
        if word[i] == currentGuess.lower():
            toBeGuessed[i] = currentGuess

    return toBeGuessed

def showScoreboard(scoreboard):
    print(scoreboard)


# Initialize the main function.
main()