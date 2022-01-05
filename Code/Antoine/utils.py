#Ce fichier contient tous les outils qui permettent de jouer mais qui ne sont pas nécessaire
#dans le prog principal, le but étant de l'alléger pour mieux comprendre
import enum

class cardType(enum.Enum):
    airplane = 1
    car = 2
    train = 3
    bike = 4
    shoes = 5

class Hand: 
    myHand = [0,0,0,0,0]

    def __init__(self, hand):
        self.myHand = hand

    def newHand(self, hand):
        self.myHand = hand
    
    def __str__(self):
        outstr = ""
        for i in range(len(self.myHand)):
            outstr += "Carte %s : %s | "%(i+1, cardType(self.myHand[i]).name)
        return outstr