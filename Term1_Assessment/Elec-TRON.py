import colorama
import random
import sys, time, os
from tqdm import tqdm
from colorama import Back, Fore, Style
colorama.init()

def Write(M):
    for char in M:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

Hierachy = {
    "Rogue":100,
    "Gladiator":1000,
    "Freeman":3000
}

Date = 0

# Classes
class User():
    def __init__(self, name, version, power=100):
        self.name = name 
        self.version = version
        self.power = power
        self.health = 100
        self.damage = 100
        self.knowledge = 0
        self.status = 'Rogue'
        self.weapon = 'Stone'
        self.disk_number = random.randint(100000, 999999)

    def losting_health(self, health_lost):
        self.health -= health_lost
        print("Your health: "+str(self.health)+"\n")

class Opponent():
    def __init__(self, name, damage=100):
        self.name = name
        self.health = 100
        self.damage = damage

# Introduction
print(Fore.RED + "The computer would like to play, you're to be overrided with care" + Fore.RESET)
print(Back.RED + "<<THIS IS YOUR WEAPON AND DISK>>" + Back.RESET)
for i in tqdm(range(3)):
    time.sleep(0.3)
Player_name = input("Your name please: ")
Player = User(Player_name, 'AL-100')
print("""
    ______
    |  ___/
    | c●●   ~
     |   ;== ~ 
     | |~     
""")
for i in tqdm(range(10)):
    time.sleep(0.3)
print([Player.name, Player.version, "Weapon:",Player.weapon, "Disk number:",Player.disk_number])
print(Back.RED + "<<THIS IS YOUR IDENTITY CARD>>" + Back.RESET)

while Player.power < Hierachy["Gladiator"]:
    Date += 1
    Write("This is the {} day in Desktop\n".format(Date))
    if Player.health <= 30:
        for i in range(3):
            print(Fore.RED + "WARNING:STARVATION")
        print(Fore.RESET)
    Scenes = open("scenes.txt", "r")
    print(Scenes.read())
    print("\n")
    Write("\nPress a number to choose where to go\n")
    Direction = int(input())
    if Direction == 1:
        Situation = random.randint(0, 3)
        if Situation == 1:
            Write("You have walked into a dark corner\n")
            Date -= 1
            continue
        else:
            Write("You have walked into nothing, begging for food?\n")
            answer = input()
            if answer.lower() == "yes":
                Player.health += random.randint(-1, 1)*10
                Player.power += 1
                print("Your health: "+Player.health)
            else:
                Player.health -= 20
                print("Your health: "+Player.health)

    if Direction == 2:
        Situation = random.randint(0, 5)
        if Situation == 1:
            Write("You have saw a wall of intellgience programs, stay and learn?\n")
            answer = input()
            if answer.lower() == "yes":
                Days = random.randint(1, 10)
                for i in range(Days):
                    Date += i
                    Write("This is the {} day in Desktop\n".format(Date))
                    knowledge_learnt = random.randint(1, 20)
                    Player.health += knowledge_learnt
                    print("Your knowledge: "+ Player.knowledge)
            else:
                Write("You choose to walk away and wated a gret opportunity\nto gain some knowledge")
        else:
            Write("""\n
A group of crazy rubbish programs saw you
They tried to rob you, but didn't succeed.
However, you have fought a serious battle.\n
            """)
            Player.losting_health(random.randint(1, 10))
    if Direction == 4:
        Situation = random.randint(0, 10)
        if Situation == 1:
            Write("""\n
You have being sent to the Colosseum 
for execution because you have fought the security guard,
you will face SHIBA - the best fighting program in this computer
            """)
            break
        else:
            Write("""\n
You look hopeless to get into the Colosseum
A security guard stopped you on the road and asked for your passpart
You didn't have one, but you escaped during their searching
of other places
        """)

print("PASS! THE GAME PAUSED")
        
        


            

            
        
                    
                
            