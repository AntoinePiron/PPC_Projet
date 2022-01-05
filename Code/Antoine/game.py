from multiprocessing import Process
from utils import *

#Le processus qui symbolise le joueur
class Player(Process):
    def run(self):
        pass

#Le processus qui se chargera de la partie 
class Game(Process):
    def run(self):
        pass

if __name__ == "__main__":
    print("Welcome to the Cambiecolo card game !")
    playerNumber = False
    numberOfPlayers = 0
    while not playerNumber:
        print("How many player will play ?")
        try:
            numberOfPlayers = int(input("(3-5 players) : "))
            if numberOfPlayers < 3 or numberOfPlayers > 5 :
                print("Please enter a valid number.")
            else:
                playerNumber = True
        except:
            print("Please enter a valid number.")
    playerHands = generateHands(playerNumber)
    
