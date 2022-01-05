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
    handTest = Hand([1,2,3,4,5])
    print(handTest)