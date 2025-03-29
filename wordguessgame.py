# Installing the random module
import random
words = ['coyote', 'zebra', 'cheetah', 'chipmunk', 'kangaroo']

# The random.choice() method is used to randomly select a word from the words list and to assign it to the answer variable
answer = random.choice(words)
board = ['_'] * len(answer)
max_guesses = 5

# We then need to determine whether or not the guessed letter is in the correct word. If it is, we loop through each letter of the word to find which position the letter is in and replace the placeholder with the guessed letter
while max_guesses > 0 and ''.join(board) != answer:
    print('\nCurrent word: ' + ' '.join(board))
    guess = input('Guess a letter: ').lower()
    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                board[i] = guess
        print('Great guess!')
    else:
        max_guesses -= 1
        print('Wrong guess... Please try again! Attempts left: '+str(max_guesses))
        if max_guesses < 1:
            print('\nYou have run out of attempts! The word was: ' + answer)
    if ''.join(board) == answer:
        print('\nCongratulations!! You guessed the word: ' + answer)
