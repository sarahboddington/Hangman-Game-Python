import os
import random

words = []

def loadWordFile(filePath): 
    global words 
    with open(filePath, 'r') as file:
        words = file.readlines()
    words = [word.strip() for word in words]

def initalSetup():
    clearTerminal()
    loadWordFile('words.txt')
    print("Welcome to Hangman!")
    mainMenu()


def mainMenu():
    print("- " * 40)
    print("Select a following option...")
    print("> New game - random word (r)")
    print("> New game - select word (s)")
    print("> Exit program - (e)")
    print("- " * 40)
    userInput = input()
    processUserInput(userInput)

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def randomWord():
    randomword = random.choice(words)
    return randomword

def inputNewWord():
    print("Please enter the word you would like to use")
    userInput = input()
    userInput = userInput.upper()
    return userInput

def newGame(chosenWord):
    clearTerminal()
    # print("DEBUG ONLY : CHOSEN WORD - "+chosenWord)
    lives = 5
    print("Starting new game...")
    unguessedWord = '_' * len(chosenWord)
    guessedletters = set()
    while lives > 0 and '_' in unguessedWord:
        if guessedletters:
            print("Previous guesses : "+(" ".join(guessedletters)))
        print("You have "+ str(lives) +" lives left")
        print()
        print(" ".join(unguessedWord))
        print()
        print("Guess a letter...")
        userInput = input()
        userInput = userInput.upper()
        clearTerminal()
        if userInput.isalpha():
            if len(userInput) != 1:
                print()
                print("Please enter a single letter...")
            else:
                if userInput in guessedletters: 
                    print("You have already guessed "+userInput)
                else:
                    guessedletters.add(userInput)
                    if userInput in chosenWord:
                        unguessedWord = list(unguessedWord)
                        for i in range(len(chosenWord)):
                            if chosenWord[i] == userInput:
                                unguessedWord[i] = userInput
                        unguessedWord = ''.join(unguessedWord)
                    else:
                        print("The word does not contain "+userInput+".")
                        lives -= 1
        else:
            print("Please enter a single letter...")
    if lives == 0:
        print("You did not correctly guess the word!")
        print("Correct word : "+chosenWord)
    if '_' not in unguessedWord: 
        print("Congratulations! You guessed the word!")
        print("Correct word : "+chosenWord)
    print()
    print("Input anything to return to the main menu")
    userInput = input()
    clearTerminal()
    mainMenu()


def processUserInput(userInput):
    clearTerminal()
    if userInput == 'R' or userInput == 'r':
        newGame(randomWord())
    elif userInput == 'S' or userInput == 's':
        newGame(inputNewWord())
    elif userInput == 'E' or userInput == 'e':
        exit()
    else:
        print("Invalid option - please try again")
        mainMenu()

if __name__ == "__main__":
    initalSetup()



