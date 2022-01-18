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
    
    def getCard(self, index):
        return self.myHand[index]
    
    def setCard(self, card, index):
        self.myHand[index] = card
    
    def fuzeHands(self, hand):
        for i in range(len(self.myHand)):
            if self.myHand[i] == 0:
                j = 0
                while j < len(hand):
                    if hand[j] != 0:
                        self.myHand[i] = hand[j]
                        hand[j] = 0
                        break
                    j += 1
    
    def winningHand(self):
        if len(set(self.myHand)) == 1: #if all the elements are the same
            return True
        return False



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

def checkInput(min, max, display):
    returnValue = 0
    while True:
        try:
            returnValue = int(input(display))
            if (returnValue > max or returnValue < min):
                print("Please enter a value between [%s,%s]"%(min,max))
                continue
            else:
                break
        except:
            print("Please enter an integer value.")
            continue
    return returnValue
