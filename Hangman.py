import random

name = input("Hey, What is your name? ")

print("Good luck", name,", I hope you win!")

words = ["moon","student","teacher","music","video"
         ,"bird","phone","movie","news"]

word = random.choice(words)

print("Guess the letters")

guesses = ""


tries = 8
print("You have",tries,"tries to guess the correct word")
while tries > 0:


    counter = 0


    for char in word:


        if char in guesses:
            print(char)

        else:
            print("_")


            counter += 1

    if counter == 0:

        print("Congratulations you won!")
        print("The word is: ", word)
        break
    print("The word consist of", len(word),"letters")
    guess = input("guess a character: ")


    guesses = guesses + guess


    if guess not in word:

        tries -= 1
        print("Ouch! you chose a wrong letter")

        if tries>1:
            print("You have", tries, "tries left")

        elif tries>0:
            print("You have", tries, "try left")

        else:
            print("you lost, you have no more tries")

