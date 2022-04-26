import random
import time

def main():
    print('Epik Dice Roller')
    player_input = input('Press d to roll dice: ')
    if player_input.lower() == 'd':
        dice_roller()
    elif player_input.lower() != 'd':
        print("bruh")
        time.sleep(3)

def dice_roller():
    number = random.randint(1, 6)
    if number == 1:
        print('You got a 1')
        print(' ')
        time.sleep(3)
        main()
    elif number == 2:
        print('You got a 2')
        print(' ')
        time.sleep(3)
        main()
    elif number == 3:
        print('You got a 3')
        print(' ')
        time.sleep(3)
        main()
    elif number == 4:
        print('You got a 4')
        print(' ')
        time.sleep(3)
        main()
    elif number == 5:
        print('You got a 5')
        print(' ')
        time.sleep(3)
        main()
    elif number == 6:
        print('You got a 6')
        print(' ')
        time.sleep(3)
        main()

main()
