import random
import pathlib

pathlib.Path("wordlist.txt").read_text(encoding="utf-8")
'adder\nblack\ncrane\nlearn\nquake\nsnake\nwyrdl\n'

# pick a word
word_list = ("loopy", "heart", "audio", "laugh", "trial", "space", "blank", "shoot", "model", "green", "range")
hidden_word = random.choice(word_list)

# repeat
for i in range (6):
    guess_word = input()
    output = ""

    if len(guess_word) != 5:
        print("Five Letter Word Please")
    else:

        # first letter
        if guess_word[0] == hidden_word[0]:
            output += "🟩"
        elif guess_word[0] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

    # second letter
        if guess_word[1] == hidden_word[1]:
            output += "🟩"
        elif guess_word[1] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

    # third letter
        if guess_word[2] == hidden_word[2]:
            output += "🟩"
        elif guess_word[2] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

    # fourth letter
        if guess_word[3] == hidden_word[3]:
            output += "🟩"
        elif guess_word[3] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

    # fifth letter
        if guess_word[4] == hidden_word[4]:
            output += "🟩"
        elif guess_word[4] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

        # result
        print(output)
        if output == "🟩🟩🟩🟩🟩":
            print('you win')
            break

print(f'you used {i+1} guesses')