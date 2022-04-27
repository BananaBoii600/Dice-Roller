import random
import time
from os import system,name

clear = lambda:system("clear") if name != "nt" else syatem("cls")

def main():
    clear()
    print('Epik Dice Roller')
    player_input = input('Press d to roll dice: ')
    
    if player_input.lower() == 'd':
        dice_roller()
    elif player_input.lower() != 'd':
        print("bruh")
        time.sleep(3)
     
def dice_roller():
    number = random.randint(1, 6)
    print(f"you got {number}")
    time.sleep(3)
    main()

if __name__ == "__main__":
    main()
