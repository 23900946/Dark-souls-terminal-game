import time
from random import *

inventory = ["Knight armor"]
health = 100
estus_flasks = 10

def health_check():
    global health
    global estus_flasks
    global player_attack
    global inventory
    if health <= 0:
        time.sleep(2)
        print("")
        print("YOU DIED")
        time.sleep(3)
        print("")
        choice = input("Do you wish to restart? (Yes/No): ")

        if choice == "Yes":
            health = 100
            estus_flasks = 10
            player_attack = randint(1,50)
            inventory.remove("Long sword")
            inventory.remove("Shield")
            if "Black knight sword" in inventory:
                inventory.remove("Black knight sword")
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
    asylum_demon()

def asylum_demon():
    global health
    global estus_flasks
    demon_health = 100
    print("You jump down from a ledge into a giant hall and encounter the Asylum demon.")
    time.sleep(5)
    print("")
    print("You must fight him if you wish to escape the Asylum.")
    time.sleep(5)
    print("")
    while demon_health > 0:
        player_attack = randint(1,50)
        boss_attack = randint(1,50)
        dodge = randint(0,1)
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
                estus_flasks -= 1

            elif estus_flasks <= 0:
                print("You have no estus flasks left.")
                print("")

            elif dodge == 0:
                print("The demon manages to strike you whilst you were trying to heal.")
                print("")
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
    bonfire()

def bonfire():
    global health
    global estus_flasks
    time.sleep(5)
    print("")
    print("You arrive at Firelink shirne and rest at the bonfire.")
    print("")
    time.sleep(3)
    Exit = "Leave"
    while True:
        print("\n Heal\n\n View inventory\n\n Leave\n")
        print("")
        time.sleep(2)
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
                print("")

            elif health >= 100:
                health = 100
                print("You are at max health")
                print("")


        elif choice == "View inventory":
            print(inventory)
            print("")

        elif choice == Exit:
            undead_berg()

        else:
            print("Please enter one of the optional choices.")
            print("")

def undead_berg():
    global health
    demon_health = 100
    mob_health = 100
    time.sleep(3)
    print("You make your way into undead burg, an abandoned town filled with hollow zombies and hell hounds.")
    print("")
    time.sleep(3)
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
            player_attack = randint(1,50)
            dodge = randint(0,1)
            mob_attack = randint(1,50)
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

                else:
                    print("The mob manages to strike you whilst you were trying to heal.")
                    health -= boss_attack
                    time.sleep(2)
                    health_check()

            else:
                print("Please enter either Attack, Block or Heal.")
                print("")

            print("")
            print("After a short battle you finally manage to defeat the hollow zombie mob.")
            print("")
            bonfire_2()

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
        print("")
        time.sleep(3)
        print("You turn a corner an encounter the Capra demon. He is blocking your exit.")
        print("")
        time.sleep(2)
        while demon_health > 0:
            player_attack = randint(1,50)
            if "Black knight sword" in inventory:
                player_attack = randint(1,50)
            elif "Long sword" in inventory:
                player_attack = randint(10,50)
            dodge = randint(0,1)
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
                    estus_flasks -= 1
                    health_check()

                else:
                    print("The demon manages to strike you whilst you were trying to heal.")
                    print("")
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
        bonfire_2()

    else:
        print("Please enter either Streets or Lower levels.")

def bonfire_2():
    global health
    global estus_flasks
    print("After exiting Undeadberg you enter a stairwell. You find another bonfire at the bottom and rest at it.")
    print("")
    time.sleep(2)
    Exit = "Leave"
    while True:
        print("\n Heal\n\n View inventory\n\n Leave\n")
        print("")
        time.sleep(2)
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
                print("")

            elif health >= 100:
                health = 100
                print("You are at max health")
                print("")

        elif choice == "View inventory":
            print(inventory)
            print("")

        elif choice == Exit:
            sens_fortress()

        else:
            print("Please enter one of the optional choices.")
            print("")

def sens_fortress():
    global health
    print("You leave the bonfire and arrive at Sen's fortress")
    print("")
    time.sleep(3)
    print("The gates of the fortress are opened for you by giant and you proceed to enter the fort.")
    print("")
    time.sleep(3)
    print("You need to reach the top of the fort, right now there are two corridors in front of you, left or right.")
    print("")
    time.sleep(3)
    choice = input("Which route do you take? (Left/Right): ")
    print("")
    if choice == "Left":
        print("You walk down the corridor on the left.")
        print("")
        time.sleep(3)
        print("You encounter a snake man who is cleary hostile.")
        print("")
        Yes = "Yes"
        while True:
            choice = input("Do you wish to attack him?: (Yes/No) ")
            print("")
            if choice == Yes:
                print("You swing your sword and kill the snake man.")
                print("")
                break

            elif choice == "No":
                print("The snake man hits you with his sword.")
                print("")
                health -= 50
                health_check()

            else:
                print("Please enter either Yes or No.")
                print("")

        print("Another snake man comes from around a corner and is running towrds you.")
        print("")
        time.sleep(2)
        Yes = "Yes"
        while True:
            choice = input("Do you wish to attack him?: (Yes/No) ")
            print("")
            if choice == Yes:
                print("You swing your sword and kill the snake man.")
                print("")
                iron_golem()

            elif choice == "No":
                print("The snake man hits you with his sword.")
                print("")
                health -= 50
                health_check()

            else:
                print("Please enter either Yes or No.")
                print("")

    elif choice == "Right":
        print("You walk down the corridor on the right.")
        print("")
        time.sleep(3)
        print("You turn round a corner and notice that there is now a huge slope that seems to lead to the top of the fort.")
        print("")
        time.sleep(3)
        print("As you make your way up the slope a boulder comes rolling down from the top which crushes you. It was a trap.")
        health = 0
        health_check()

    else:
        print("Please enter either Left or Right.")
        print("")

def iron_golem():
    golem_health = 100
    print("You finally reach the roof of the fortress and you find the Iron golem is standing who wants to engage you in battle.")
    print("")
    while golem_health <= 0:
        if "Black knight sword" in inventory:
            player_attack = randint(1,50)
        elif "Long sword" in inventory:
            player_attack = randint(10,50)
        boss_attack = randint(1,50)
        dodge = randint(0,1)
        choice = input("Do you wish to Attack/Block/Heal?: ")
        print("")
        print(f"Your health: {health}")
        print(f"Iron golem health: {golem_health}")
        print("")
        if choice == "Attack":
            demon_health -= player_attack
            print("You swing your sword and successfully hit them.")
            print("")
            time.sleep(2)
            print("The golem retialiates.")
            print("")
            health -= boss_attack
            health_check()

        elif choice == "Block":
            health -= boss_attack
            health += 10
            time.sleep(2)
            print("The golem attacks.")
            print("")
            health_check()

        elif choice == "Heal":
            if dodge == 1:
                print("You manage to heal without the golem hitting you.")
                print("")
                time.sleep(2)
                health += 20
                estus_flasks -= 1

            else:
                print("The golem manages to strike you whilst you were trying to heal.")
                print("")
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
    print("The Iron golem falls to the floor. You are then picked up by some gargolyes who take you away from the fort.")
    time.sleep(4)
    anor_londor()

def anor_londor():
    global health
    smough_health = 100
    ornstein_health = 100
    print("")
    print("You are dropped off in Anor londor, the city where the former seat of power of the gods is located.")
    print("")
    time.sleep(5)
    print("You make your way through the city and enter the catherdral.")
    print("")
    time.sleep(4)
    print("Inside the catherdral you encounter Dragon slayer Ornstein and Executioner Smough.")
    print("")
    time.sleep(3)
    print("They are your final test.")
    print("")
    time.sleep(3)
    while smough_health > 0 and ornstein_health > 0:
        if "Black knight sword" in inventory:
            player_attack = randint(10,50)
        elif "Long sword" in inventory:
            player_attack = randint(1,50)
        dodge = randint(0,1)
        choice = input("Do you wish to Attack/Block/Heal?: ")
        print("")
        print(f"Your health: {health}")
        print(f"Smough health: {smough_health}")
        print(f"Ornstein health: {ornstein_health}")
        print("")
        if choice == "Attack":
            print("You engage in battle with the duo and land successfull hits.")
            print("")
            smough_health -= player_attack
            ornstein_health -= player_attack
            health_check()
            time.sleep(2)
            print("They retialiate.")
            print("")
            time.sleep(2)

        elif choice == "Block":
            time.sleep(2)
            print("They attack you.")
            print("")
            health -= boss_attack
            health += 10
            health_check()

        elif choice == "Heal":
            if dodge == 1:
                print("You manage to heal without them hitting you.")
                print("")
                time.sleep(2)
                health += 20
                estus_flasks -= 1

            else:
                print("They manage to strike you whilst you were trying to heal.")
                print("")
                health -= boss_attack
                time.sleep(2)
                health_check()

        elif smough_health <= 0 and ornstein_health <= 0:
            break

        else:
            print("Please enter either Attack, Block or Heal.")
            print("")

    print("VICTORY ACHIEVED")
    print("")
    time.sleep(5)
    print("After a tough fight you have finally defeated Ornstein and Smough.")
    time.sleep(3)
    ending()

def ending():
    print("")
    print("You ascend the elevator at the end of the room and open the chamber to the room of princess Gywnavere.")
    print("")
    time.sleep(3)
    print("You have now beaten the game.")

opening()
