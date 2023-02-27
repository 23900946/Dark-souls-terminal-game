import time
from random import *

inventory = ["Knight armor"]
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
            health = 100
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
            print("You do nothing")
            print("")

        else:
            print("Please enter either Yes or No")
            print("")

def undead_asylum():
    global health
    time.sleep(5)
    print("")
    print("You unlock the cell and enter the corridor where you manage to find a sword and shield. Both are added to your inventory.")
    inventory.append("Long sword")
    inventory.append("Shield")
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
            print("")
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

    time.sleep(3)
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
                print("")
                time.sleep(2)
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
    Exit = "Leave"
    while True:
        print("Heal\n View inventory\n Leave\n")
        print("")
        choice = input("What do you wish to do?: ")
        print("")
        if choice == "Heal":
            if estus_flasks > 0:
                print(f"Your current health is: {health}")
                time.sleep(2)
                print("")
                print("You gulp down an estus flask.")
                print("")
                time.sleep(2)
                estus_flasks -= 1
                health += 30
                print(f"Your health now is: {health}")
                print("")

            elif estus_flasks <= 0:
                print("You have no estus flasks left.")

        elif choice == "View inventory":
            print(inventory)
            print("")

        elif choice == Exit:
            undead_berg()

        else:
            print("Please enter one of the optional choices.")
            print("")

def undead_berg():
    global player_attack
    global boss_attack
    global dodge
    global health
    demon_health = 100
    mob_health = 100
    mob_attack = randint(1,50)
    time.sleep(3)
    print("")
    print("You make your way into undead burg, an abandoned town filled with hollow zombies and hell hounds.")
    print("")
    print("You can either make your way through the streets or thorugh the lower levels of the city.")
    time.sleep(3)
    print("")
    choice = input("Which do you chose? (Streets/Lower levels): ")
    print("")
    if choice == "Streets":
        time.sleep(2)
        print("Whilst making you way through the streets of the city you are ambushed by a mob of hollow zombies.")
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

            print("")
            print("After a short battle you finally manage to defeat the hollow zombie mob.")
            print("")
            anor_londor()

    elif choice == "Lower levels":
        time.sleep(2)
        print("You go down some stairs and enter the lower levels of the city.")
        print("")
        time.sleep(3)
        print("You stumble upon and open a chest containing a Black Knight sword.")
        time.sleep(3)
        print("")
        print("This sword deals more damage so you discard your Long sword.")
        inventory.append("Black knight sword")
        inventory.remove("Long sword")
        player_attack = randint(10,50)
        print("")
        time.sleep(3)
        print("You turn a corner an encounter the Capra demon. He is blocking your exit.")
        print("")
        time.sleep(2)
        while demon_health > 0:
            choice = input("Do you wish to Attack/Block/Heal?: ")
            print("")
            print(f"Your health: {health}")
            print(f"Capra demon health: {demon_health}")
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
                    print("")
                    time.sleep(2)
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
        print("The demon drops dead.")
        anor_londor()

def anor_londor():
    smough_health = 100
    ornstein_health = 100
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
            print("You engage in battle with the duo and land successfull hits.")
            smough_health -= player_attack
            ornstein_health -= player_attack
            health_check()

        elif choice == "Block":
            print("")
            health -= boss_attack
            health += 10
            health_check()

        else:
            print("Please enter either Attack, Block or Heal.")

    print("")
    print("VICTORY ACHIEVED")
    time.sleep(5)
    print("")
    print("")
    ending()

def ending():
    print("")
    print("You ascend the elevator at the end of the room and open the chamber to the room of princess Gywnavere.")
    print("")
    time.sleep(3)
    print("You have now beaten the game.")

opening()
