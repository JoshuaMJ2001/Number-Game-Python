import random

def mainMenu():
	running = True
	while running == True:
		print('''Welcome to the Menu - What would you like to do?
(1) Roll One Dice
(2) Roll Two Die
(3) Flip and Guess a Coin
(4) Guess a Random Number Between 1 and 100
(5) Guess a Random Number Between 1 and 100
(6) Guess a Random Number Between 1 and 100
(7) Pick A Card
(8) Quit''')
		if choice == 1:
			dice()
        elif choice == 2:
            die()
        elif choice == 3:
            coin()
        elif choice == 4:
            number_10()
        elif choice == 5:
            number_100()
        elif choice == 6:
            number_1000
		elif choice == 7:
            card()
		elif choice == 8:
            running = False
        else:
            menu()

mainMenu()
