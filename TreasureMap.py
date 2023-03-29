from tkinter.tix import COLUMN


row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
pos = str(position)
num1 = int(pos[0]) - 1
num2 = int(pos[1]) - 1
row = map[num2]
row[num1]="X"
print(f"{row1}\n{row2}\n{row3}")