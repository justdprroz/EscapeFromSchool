import os
import msvcrt
print("Hello!")
clear = lambda: os.system('cls')
clear()
l = 0
menu = [["@", "@", "@", "@", "@", "@", "@", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], ["@", " ", " ", " ", " ", " ", "@", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", "O"], ["@", "s", "t", "a", "r", "t", "@", "m", "u", "s", "i", "c", "O", "c", "l", "o", "s", "e", "O"], ["@", " ", " ", " ", " ", " ", "@", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", "O"], ["@", "@", "@", "@", "@", "@", "@", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]]
for i in range(len(menu)):
    for j in range(len(menu[i])):
        print(menu[i][j], end="")
    print("")
while True:
    pressedKey = msvcrt.getch()
    if pressedKey in (b'\x00', b'\xe0'):  # arrow or function key prefix?
        pressedKey = msvcrt.getch()
    if pressedKey == b'K':
        if l != 0:
            clear()
            for i in range(len(menu)):
                for j in range(len(menu[i])):
                    if menu[i][j] == "@":
                        menu[i][j] = "O"
                if i == 0 or i == 4:
                    for n in range(7):
                        menu[i][6 * (l - 1) + n] = "@"
                if i == 1 or i == 2 or i == 3:
                    menu[i][6 * (l - 1)] = "@"
                    menu[i][6 * (l)] = "@"
            for i in range(len(menu)):
                for j in range(len(menu[i])):
                    print(menu[i][j], end="")
                print("")
            l -= 1
    elif pressedKey == b'M':
        if l != 2:
            clear()
            for i in range(len(menu)):
                for j in range(len(menu[i])):
                    if menu[i][j] == "@":
                        menu[i][j] = "O"
                if i == 0 or i == 4:
                    for n in range(7):
                        menu[i][6 * (l + 1) + n] = "@"
                if i == 1 or i == 2 or i == 3:
                    menu[i][6 * (l + 1)] = "@"
                    menu[i][6 * (l + 2)] = "@"
            for i in range(len(menu)):
                for j in range(len(menu[i])):
                    print(menu[i][j], end="")
                print("")
            l += 1