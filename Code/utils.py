import enum
import random

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

class Offers: 
    playerID = ""
    numberOfcards = 0

    def __init__(self, ID, num):
        self.playerID = ID
        self.numberOfcards = num

def generateHands(numberOfPlayers):
    numberOfCards = numberOfPlayers * 5
    cards = []
    while len(cards) < numberOfCards :
        newCard = int(random.randint(1,numberOfPlayers))
        if cards.count(newCard) == 5: #Si la carte est déjà présente 5 fois dans la génération 
            continue
        else:
            cards.append(newCard)
    hands = []
    for i in range(0, len(cards), 5):
        hands.append(Hand(cards[i:i+5]))
    return hands