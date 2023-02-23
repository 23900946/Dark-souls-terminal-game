import time
from random import *

health = 100
current_health = health
estus_flasks = 5
player_attack = randint(1,50)
boss_attack = randint(1,50)

def health_check():
    global health
    if health <= 0:
        time.sleep(2)
        print("")
        print("YOU DIED")
        time.sleep(3)
        print("")
        choice = input("Do you wish to restart? (Yes/No): ")

        if choice == "Yes":
            opening()

        elif choice == "No":
            exit()

        else:
            print("Please enter either Yes or No")

def opening():
    print ("  _______      _____     ______     _     __    _____   _______   _    _   _       _____  ")
    print (" |  ____ \    / ___ \   |  __  \   | |   / /   |  ___| |  ___  | | |  | | | |     |  ___| ")
    print (" | |    | |  | /   \ |  | |  | |   | |  / /    | |     | |   | | | |  | | | |     | |     ")
    print (" | |    | |  | |   | |  | |  | |   | |_/ /     | |___  | |   | | | |  | | | |     | |___  ")
    print (" | |    | |  | |___| |  | |__| |   |  _ |      |___  | | |   | | | |  | | | |     |___  | ")
    print (" | |    | |  |  ___  |  |  ___ \   | | \ \         | | | |   | | | |  | | | |         | | ")
    print (" | |____| |  | |   | |  | |   \ \  | |  \ \     ___| | | |___| | | |__| | | |___   ___| | ")
    print (" |_______/   |_|   |_|  |_|    \_\ |_|   \_\   |_____| |_______| |______| |_____| |_____| ")
    time.sleep(5)
    print("")
    print("")
    print ("You awaken in the undead asylum after a knight throws a hollow corpse into your cell.")
    print("")
    time.sleep(5)
    Yes = "Yes"
    while True:
        choice = input("Do you wish to inspect the corpse? (Yes/No): ")
        print("")
        if choice == Yes:
            print ("You recieved the key to your cell, now you can escape.")
            undead_asylum()
            break

        elif choice == "No":
            print ("You do nothing")
            print("")

        else:
            print ("Please enter either Yes or No")
            print("")

def undead_asylum():
    global health
    time.sleep(5)
    print("")
    print("You unlock the cell and enter the corridor where you manage to find a sword and shield.")
    print("")
    time.sleep(5)
    print("You notice that there is a hollow zombie walking towards you.")
    print("")
    time.sleep(5)
    Yes = "Yes"
    while True:
        choice = input("Do you wish to attack it? (Yes/No): ")
        print("")
        if choice == Yes:
            time.sleep(3)
            print("You swing your sword which kills the hollow zombie instantly.")
            break

        elif choice == "No":
            time.sleep(2)
            print("The hollow zombie hits you")
            print("")
            health -= 50
            health_check()

        else:
            print("Please enter either Yes or No.")
            print("")

    print("")
    print("You make your way out of the corridor and into the courtyard.")
    time.sleep(5)
    print("")
    print("You make you way up some stairs where you bump into the knight you saw eariler and he gives you some estus flasks.")
    print("")
    time.sleep(5)
    print("This means that you can now restore any health you have lost.")
    print("")
    time.sleep(5)
    asylum_demon_fight()

def asylum_demon_fight():
    global player_attack
    global boss_attack
    global dodge
    global health
    demon_health = 100
    dodge = randint(0,1)
    print("You jump down from a ledge and encounter the Asylum demon.")
    time.sleep(5)
    print("")
    print("You must fight him if you wish to escape the Asylum.")
    time.sleep(5)
    print("")
    while demon_health > 0:
        choice = input("Do you wish to Attack/Block/Heal?: ")
        print("")
        print(f"Your health: {health}")
        print(f"Asylum demon health: {demon_health}")
        print("")
        if choice == "Attack":
            demon_health -= player_attack
            print("You swing your sword and successfully hit them.")
            print("")
            time.sleep(2)
            print("The demon retialiates.")
            print("")
            health -= boss_attack
            health_check()

        elif choice == "Block":
            health -= boss_attack
            health += 10
            time.sleep(2)
            print("The demon attacks.")
            print("")
            health_check()

        elif choice == "Heal":
            if dodge == 1:
                print("You manage to heal without the demon hitting you.")
                health += 20
                health_check()

            else:
                print("The demon manages to strike you whilst you were trying to heal.")
                health -= boss_attack
                time.sleep(2)
                health_check()

        elif demon_health == 0:
            break

        else:
            print("Please enter either attack or block.")
            print("")

    print("")
    print("VICTORY ACHIEVED")
    time.sleep(5)
    print("")
    print("The demon drops dead. You exit the asylum and you are picked up by a giant crow and taken to firelink shirne.")
    firelink_shirne()

def firelink_shirne():
    global health
    global estus_flasks
    time.sleep(5)
    print("")
    print("You arrive at fireLink shire and rest at the bonfire.")
    time.sleep(5)
    print("")
    print(f"Your current health is: {health}")
    choice = input("Do you wish to heal? (Yes/No): ")
    print("")
    if choice == "Yes":
        print("You gulp down an estus flask.")
        estus_flasks -= 1
        health += 30
        undead_berg()

    elif choice == "No":
        undead_berg()

    elif estus_flasks <= 0:
        print("You have no estus flasks left.")

    else:
        print("Please enter either Yes or No.")
        print("")

def undead_berg():
    mob_health = 100
    mob_attack = randint(1,50)
    time.sleep(3)
    print("")
    print("You make your way into undead burg, an abandoned town filled with hollow zombies and hell hounds.")
    print("")
    print("Whilst making you way through the city you are ambushed by a mob of hollow zombies.")
    print("")
    while mob_health > 0:
        choice = input("Do you wish to Attack/Block/Heal?: ")
        print("")
        if choice == "Attack":
            mob_health -= player_attack
            time.sleep(2)
            print("You attack the mob.")
            health -= mob_attack
            time.sleep(2)
            print("")
            print("The hollow zombies hit you with their swords.")
            health_check()

        elif choice == "Block":
            health -= mob_attack
            health += 10
            print("The hollow zombies hit you with their swords.")
            health_check()

        elif mob_health <= 0:
            print("You finally managed to defeat the hollow zombies.")
            time.sleep(3)
            break

        elif choice == "Heal":
            if dodge == 1:
                print("You manage to heal without them hitting you.")
                health += 20
                health_check()

            else:
                print("The mob manages to strike you whilst you were trying to heal.")
                health -= boss_attack
                time.sleep(2)
                health_check()

        else:
            print("Please enter either Attack, Block or Heal.")

def anor_londor():
    print("")
    print("You are dropped off in Anor londor, the city where the former seat of power of the gods is located.")
    print("")
    time.sleep(5)
    print("You make your way through the city and enter the catherdral.")
    print("")
    time.sleep(5)
    print("Inside the catherdral you encounter Dragon slayer Ornstein and Executioner Smough.")
    time.sleep(3)
    print("They are your final test.")
    time.sleep(3)
    while smough_health > 0 and ornstein_health > 0:
        choice = input("Do you wish to Attack/Block/Heal?: ")
        print("")
        if choice == "Attack":
            break

        else:
            print("")

opening()
