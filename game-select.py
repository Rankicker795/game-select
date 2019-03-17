import sys
import time
import random

def arrayGenerator():
    count = input("Enter a number --> ")
    try:
        count = int(count)
    except:
        sys.exit("Not a number, dumbass! Exiting!!!")
    if count <= 0:
        sys.exit("Negative Nancy! Exiting!!!")
    else:
        game_ls = [ ]
        x = 0
        while (x < count):
             game_title = input("Enter a game title -> ")
             game_ls.append(game_title)
             x += 1
    return game_ls

def gameChoice(game_ls_length):
    num = random.randint(0,game_ls_length - 1)
    return num

def magicCompScreen(game_ls, num):
    game = game_ls[num]
    time.sleep(1)
    print("-----------------------------------------------")
    time.sleep(1)
    print("|                                             |")
    time.sleep(1)
    print("|                                             |")
    time.sleep(1)
    print("|                                             |")
    time.sleep(1)
    print("|    {}                                       |".format(game))
    time.sleep(1)
    print("|                                             |")
    time.sleep(1)
    print("|                                             |")
    time.sleep(1)
    print("|                                             |")
    time.sleep(1)
    print("-----------------------------------------------")
    time.sleep(1)
    print("     /                                    \    ")   
    time.sleep(1)
    print("-----------------------------------------------")
    time.sleep(1)
    print("|  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |")
    time.sleep(1)
    print("|---------------------------------------------|")
    time.sleep(1)
    print("|   |  |  |  |  |  |  |  |  |  |  |  |  |   | |")   
    time.sleep(1)
    print("|---------------------------------------------|")
    time.sleep(1)
    print("|   | |  |                          |  |  |   |")
    time.sleep(1)
    print("----------------------------------------------|\n")
    print("###--- Thanks for playing!               ---###")
        

def main():
    print("###--- Welcome to the Game Selector 9000 ---###")
    print("###--- for indecisvie gamers! Please     ---###")
    print("###--- enter a number of games to        ---###")
    print("###--- select from.                      ---###")
    game_ls = arrayGenerator()
    print("###--- Now calling upon the magic        ---###")
    print("###--- computer to make your choice!!!   ---###")
    game_ls_length = len(game_ls)
    num = gameChoice(game_ls_length)
    magicCompScreen(game_ls, num)

if __name__ == "__main__":
    main()
 
