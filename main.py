import random
import string
print('H A N G M A N')
print('')
results = []
decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
while decision != "exit":
    if decision == "results":
        win = results.count('win')
        lost = results.count('lost')
        print(f'You won: {win} times.')
        print(f'You lost: {lost} times.')
    elif decision == "play":
        rand = ['python', 'java', 'swift', 'javascript']
        word = random.choice(rand)
        hint = []
        guessed = []
        for i in range(len(word)):
            hint.append('-')
        i = 1
        while i <= 8:
            w = ''.join(hint)
            if '-' not in hint:
                results.append('win')
                print(f'You guessed the word {w}!')
                print('You survived!')
                break
            else:
                print(w)
            guess = input('Input a letter: ')
            if len(guess) != 1:
                print('Please, input a single letter.')
            elif guess not in string.ascii_lowercase:
                print('Please, enter a lowercase letter from the English alphabet.')
            elif guess in hint or guess in guessed:
                print("You've already guessed this letter.")
            elif guess not in word and guess not in hint:
                print("That letter doesn't appear in the word")
                if i == 8:
                    results.append('lost')
                    print('You lost!')
                    break
                i += 1
            else:
                hint = [x if x == guess or x in hint else "-" for x in word]
            guessed.append(guess)
            if '-' in hint:
                print('')
    decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
