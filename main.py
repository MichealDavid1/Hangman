import random
import string

print("H A N G M A N")
choice = ["play", "exit"]
choose_to_play = input('Type "play" to play the game, "exit" to quit: ')
while choose_to_play not in choice:
    choose_to_play = input('Type "play" to play the game, "exit" to quit: ')
while choose_to_play == "play":
    list_of_word = ['python', 'java', 'kotlin', 'javascript']
    secret = random.choice(list_of_word)
    x = len(secret)
    hint = []
    for i in range(x):
        hint.append("-")
        i += 1
    hint = "".join(hint)
    game_period = len(set(secret))
    letter = ""
    j = 1
    guessed_letters = []
    while "-" in hint:
        hint = [x if x == letter or x in hint else "-" for x in secret]
        hint = "".join(hint)
        if "-" not in hint:
            break
        print()
        print(hint)
        letter = input("Input a letter: ")
        if len(letter) > 1:
            print("You should input a single letter")
        elif letter not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
        elif letter in hint or letter in guessed_letters:
            print("You've already guessed this letter")
        while (letter not in secret and letter in string.ascii_lowercase) and j <= 8 and letter not in guessed_letters:
            print("That letter doesn't appear in the word")
            j += 1
            break
        if (letter not in secret and letter in string.ascii_lowercase) and j > 8 and (letter not in guessed_letters):
            break
        guessed_letters.append(letter)
    if "-" not in hint:
        print()
        print(hint)
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")
    print()
    choose_to_play = input('Type "play" to play the game again, "exit" to quit: ')
    while choose_to_play not in choice:
        choose_to_play = input('Type "play" to play the game again, "exit" to quit: ')
