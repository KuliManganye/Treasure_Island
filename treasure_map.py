# this is a simple treasure map where x marks the spot

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? Input 2 numbers, the first one represents the column and the second one represents the row")

# we will prompt the user to input 2 numbers, the first one will represent the column while the 2nd one represents the row in which the x will be placed
column = int(position[0])
row = int(position[1])

map[row - 1][column -1] = "X"

print(f"{row1}\n{row2}\n{row3}")