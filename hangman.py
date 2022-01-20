secret_word="SaiPriya"
letter_guessed=" "
count_guessnumber=8
while count_guessnumber>0:
    guess_letter=input("enter the guess letter:")
    if guess_letter in secret_word:
        print(f"correct there is one or more {guess_letter} in the secreat word.")
    else:
        count_guessnumber-=1
        print(f"correct there is one or more {guess_letter} in the secreat word.{count_guessnumber} turn(s) lift.")
    letter_guessed=letter_guessed+guess_letter
    wrong_lettercount=0
    for letter in secret_word:
        if letter in letter_guessed:
            print(f"{letter}",end="")
        else:
            print("_",end="")
            wrong_lettercount+=1
    print(" ")
    if wrong_lettercount==0:
        print(f"congratulations! the secret  was:{secret_word} you won!. ")
        break
else:
    print("sorry you didn't win it this time.try again! ")