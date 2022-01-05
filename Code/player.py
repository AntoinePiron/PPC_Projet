import multiprocessing
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
    
    def __str__(self) -> str:
        outstr = ""
        for i in range(len(self.myHand)):
            outstr += "Carte %s : %s | "%(i, cardType(self.myHand[i].name))
        return outstr


if __name__ == "__main__":
    testHand = Hand([1,2,3,4,5])
    print(testHand)