import random
# and selecting a word randomly
predef_words = ['consistency', 'minfulness', 'discipline', 'hardwork', 'resilience']
ran_selec = random.choice(predef_words)
#setting up the parameters for the selected word
display_word = ['_']*len(ran_selec)
guesses = []
max_guesses = 6
curr_guess = 0
#the game mechanism
print("Welcome to my Hangman Game🎮\nGuess the word correctly to Win(Note: One letter at a time)")
while curr_guess<max_guesses and '_' in display_word:
    print("\nWord: ",' '.join(display_word))
    print("\nGuesses: ",' '.join(guesses))
    print("Remaining Guesses: ",(max_guesses-curr_guess))
    guess = input("Enter a letter: ").lower()

    if(len(guess)!=1 or not guess.isalpha()):
        print("Only single alphabets are valid!🫤")
        guesses.append(guess+"❌")
        curr_guess+=1
        continue

    if ((guess+"✅" in guesses) or (guess+"❌" in guesses)):
        print("Letter already guessed!🫤")
        continue

    if guess in ran_selec:
        print("Correct✅")
        guesses.append(guess+"✅")
        for i in range(len(ran_selec)):
            if ran_selec[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong❌Guess!")
        guesses.append(guess+"❌")
        curr_guess+=1
#result declaration
if '_' in display_word:
    print("\nBetter Luck Next Time😞\nYour word was: ",ran_selec)
else:
    print("\n🎉Congrats🥳\n",ran_selec," is the correct word!")