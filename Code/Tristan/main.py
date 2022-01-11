from multiprocessing import Process
from utils import *

#Le processus qui symbolise le joueur
class Player(Process):
    hand = Hand([0,0,0,0,0])

    def __init__(self, hand):
        super().__init__()
        self.hand = hand

    def run(self):
        print("Player process started")
        print("Player hand : " + self.hand.__str__())

        

#Le processus qui se chargera de la partie 
class Game(Process):

    def run(self):
        while True:
            pass

if __name__ == "__main__":
    print("Welcome to the Cambiecolo card game !")
    numberOfPlayers = 0
    while True:
        print("How many player will play ?")
        try:
            numberOfPlayers = int(input("(3-5 players) : "))
            if numberOfPlayers < 3 or numberOfPlayers > 5 :
                print("Please enter a valid number.")
            else:
                break
        except:
            print("Please enter a valid number.")
    
    playerHands = generateHands(numberOfPlayers)
    playerProcesses = []
    for h in playerHands:
        playerProcesses.append(Player(h))

    
