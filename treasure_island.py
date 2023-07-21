print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

door = input("You have 2 doors infront of you, which one will you choose, Left or Right? ")
door = door.lower()

if door == "left":
    door = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or type 'swim' to swim to the island. ")
    if door == "wait":
        door = input("You have arrived at the island unharmed. There is a house with 3 door. One red, one yellow and one blue. Type the colour of the door you choose ")
        if door == "red":
            print("Burned by Fire. GAME OVER")
        elif door == "blue":
            print("Eaten by beasts. GAME OVER")
        elif door == "yellow":
            print("YOU WIN!")
        else:
            print("GAME OVER")
    else:
        print("Attached by Trout. GAME OVER")
else:
    print("Fall into a hole. GAME OVER")