import random
import string

WORDLIST_FILENAME = "words.txt"

def clearScreen():
    number = 80
    while number > 0:
        print ""
        number -= 1
    return

def loadWords():
    print "Loading word list from file..."
	# inFile: file
    inFile = open('/home/timgriffith/Dropbox/mit_python/words.txt','r', 0)
	# line: string
    line = inFile.readline()
	# wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    result = []
    for char in secretWord:
		if char in lettersGuessed:
			result.append(char)
			if char not in result:
				count += 1
    if len(result) == len(secretWord):
		return True
    else:
		return False


def getGuessedWord(secretWord, lettersGuessed):
    result = []
    for char in secretWord:
		if char not in lettersGuessed:
			char = ' _ '
		result.append(char)
    return ' '.join(map(str, result))


def getAvailableLetters(lettersGuessed):
    alreadyGuessed = []
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for char in lettersGuessed:
		if char not in alreadyGuessed:
			alpha.remove(char)
		alreadyGuessed.append(char)
    return ''.join(map(str, alpha))
    

def hangman(secretWord):
    clearScreen()
    guesses = 8
    guessed = ''
    results = []
    guess = ''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word ' + str(len(secretWord)) + ' letters long.'
    print '-------------'
    while isWordGuessed(secretWord,results) == False:
        print 'You have ' + str(guesses) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(results)
        guess = raw_input("Please guess a letter: ")
	guess = guess.lower()
        results.append(guess)
        if guess in guessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord,results)
            outputGraphics(guesses)
            continue    
        if guesses <= 1:
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord,results)
            print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
            outputGraphics(guesses)
            break
        if guess in secretWord:
            print 'Good guess: ' + getGuessedWord(secretWord,results)
            outputGraphics(guesses)
        if guess not in secretWord:
            guesses -= 1
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord,results)
            outputGraphics(guesses)
        guessed += guess
    if isWordGuessed(secretWord,results) == True:
        print 'Congratulations, you won!'
        
def outputGraphics(guesses):
    if guesses == 7:
        print('|---------|                 |------------------|')
        print('|                           |You got 7 guesses!|')
        print('|                           |Save me pal!      |')
        print('|                           |------------------|')
        print('|                           /')
        print('|                          O')
        print('|  ______                 /|\\')
        print('| |      |                 |')
        print('|_|______|________________/_\\')
    elif guesses == 6:
        print('|---------|               |-----------------------|')
        print('|                         |You got 6 guesses!     |')
        print("|                         |C'mon you can save me! |")
        print('|                         |-----------------------|')
        print('|                         /')
        print('|                        O')
        print('|  ______               /|\\')
        print('| |      |               |')
        print('|_|______|______________/_\\__')
    elif guesses == 5:
        print('|---------|           |------------------|')
        print('|                     |You got 5 guesses!|')
        print("|                     |it's close to me! |")
        print('|                     |------------------|')
        print('|                     /')
        print('|                    O')
        print('|  ______           /|\\')
        print('| |      |           |')
        print('|_|______|__________/_\\________')
    elif guesses == 4:
        print('|---------|         |------------------------------|')
        print('|                   |You got 4 guesses!            |')
        print('|                   |are you sure you can save me! |')
        print('|                   |------------------------------|')
        print('|                   /')
        print('|                  O')
        print('|  ______         /|\\')
        print('| |      |         |')
        print('|_|______|________/_\\__________')
    elif guesses == 3:
        print('|---------|        |------------------|')
        print('|                  |You got 3 guesses!|')
        print("|                  |This isn't funny! |")
        print('|                  |------------------|')
        print('|                  /')
        print('|                 O')
        print('|  ______        /|\\')
        print('| |      |        |')
        print('|_|______|_______/_\\___________')
    elif guesses == 2:
        print('|---------|      |------------------|')
        print('|                |You got 2 guesses!|')
        print("|                |I don't wanna die!|")
        print('|                |------------------|')
        print('|               /')
        print('|              O')
        print('|  ______     /|\\')
        print('| |      |     |')
        print('|_|______|____/_\\______________')
    elif guesses == 1:
        print('|---------|')
        print('|    |      |-----------------------|')
        print("|    |      |You've your last guess!|")
        print('|    O -----|hasta la vista baby!   |')
        print('|   /|\\     |-----------------------|')
        print('|    |')
        print('|  _/_\\__')
        print('| |      |     ')
        print('|_|______|______________________')
    elif guesses == 0:
        print('|---------|')
        print('|    |   ')
        print('|    |            Your hero died. Game over!')
        print('|    O')
        print('|   /|\\')
        print('|    |')
        print('|   / \\')
        print('| |\\   /|     ')
        print('|_|_\\_/_|______________________')
        
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
