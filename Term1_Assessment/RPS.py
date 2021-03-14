import sys, time, random
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

def Write(M):
    for char in M:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

Write("Play scissors, paper and rock? ")
Wish = input()
if Wish.lower() == "no":
    print("Ohh, I wanted to play...")
    exit()
while True:
    Options = ["scissors", "paper", "rock"]
    Computer_choice = random.choice(Options)
    Player_choice = input("Your choice?\n")
    if Player_choice.lower() == "no":
        Write("Come on, you can win!\nOkay, I'll play you next time...\n")
        break

    print(Computer_choice)
    if Player_choice not in Options:
        print(Fore.YELLOW + "Shut up!Give me a valid answer!!!")
    if Player_choice.lower() == "scissors" and Computer_choice == "paper":
        Write("You've cut him open!")
        print(Fore.GREEN + "\nResult: WIN")
    if Player_choice.lower() == "paper" and Computer_choice == "scissors":
        Write("Whoo!You've lost")
        print(Fore.RED + "\nResult: LOSS")
    if Player_choice == "rock" and Computer_choice == "scissors":
        Write("You've crushed him!")
        print(Fore.GREEN + "\nResult: WIN")
    if Player_choice == "scissors" and Computer_choice == "rock":
        Write("He turned you into a pile of metal!")
        print(Fore.RED + "\nResult: LOSS")
    if Player_choice == "paper" and Computer_choice == "rock":
        Write("You have encircled him!")
        print(Fore.GREEN + "\nResult: WIN")
    if Player_choice == "rock" and Computer_choice == "paper":
        Write("Gets turned into a dumpling")
        print(Fore.RED + "\nResult: LOSS")
    if Player_choice == Computer_choice:
        Write("Oh, that's close!")
        print(Fore.CYAN + "\nResult: DRAW")






