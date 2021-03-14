import os, random
os.system("clear")

#Initialise
words = ["UBUNTO", "SALADIN", "OPAQUE", "PERIPHRALS", "CARBONHYDRATES", "CORRECT", "APPLE", "BANANA"]
word = random.choice(words)
guess = "-------------------"
wrong_letters = ""

#Print header
print("HANGMAN\n")

while True:
    print(f"Current Guess: {guess}")
    print(f"Wrong Guesses: {wrong_letters}")

    if len(wrong_letters) == 0:
        print("""
    -------
    |    
    |    |
    |    |
    |   
    |
    |
    |
    ________________""")

    letter = input("\nPlease enter a letter. >").upper()
    if letter == word:
        print("YOU WON'T BE THIS LUCKY NEXT TIME!")
        exit()
    if letter in word:
        temp = ""
        for index in range(len(word)):
            if letter == word[index]:
                temp += letter
            elif guess[index] != "-" :
                temp += guess[index]
            else:
                temp += "-"
        guess = temp
    else:
        wrong_letters += letter

    

    if len(wrong_letters) == 1:
            print("""
    -------
    |    0
    |    |
    |    |
    |   
    |
    |
    |
    ________________""")

    if len(wrong_letters) == 2:
            print("""
    -------
    |    0
    |   \\|/
    |    |
    |   
    |
    |
    |
    ________________""")

    if len(wrong_letters) == 3:
            print("""
    -------
    |    0
    |   \\|/
    |    |
    |   /
    |
    |
    |
    ________________""")

    if len(wrong_letters) == 4:
            print("""
    -------
    |    0
    |   \\|/
    |    |
    |   / \\
    |
    |
    |
    ________________""")


    if len(wrong_letters) >= 5:
        print("""
    -------
    |    |
    |    0
    |   \\|/
    |    |
    |   / \\
    |
    |
    ________________""")
        print("Done, you're doomed!")
        exit()

    if word == guess:
        print("YOU HAVE WON YOUR FREEDOM FOR THE DAY!")
        exit()

