
"""
AUTHOR

    Abhishek Rajput <Abhishekrajput676@gmail.com>
    
This module contains the player class with all the functionalities that a player will have during the game play.
It also contains the methods to show the result to the player.

"""

class Player:

    def __init__(self,hand=[],money=100):
         self.hand = hand
         self.score = self.setScore()
         self.money = money
         self.bet = 0

    def __str__(self):
        currentHand=""
        for card in self.hand:
            currentHand+=card + " "
        finalStatus = currentHand + "\tScore : " + str(self.score)
        return finalStatus
    
    def setScore(self):
        self.score=0
        faceCardsDict={"A":11,"J":10,"Q":10,"K":10,"2":2,"3":3,"4":4,
                        "5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
        aceCounter = 0
        for card in self.hand:
            self.score += faceCardsDict[card]
            if card == "A":
                aceCounter+=1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score

    def hit(self,card):
        self.hand.append(card)
        self.score=self.setScore()

    def play(self,newHand):
        self.hand = newHand
        self.score = self.setScore()

    def betMoney(self,amount):
        self.money -= amount
        self.bet += amount

    def win(self,result):
        if result == True:
            print("\n\n\t----------Whoa!! You Won!!----------")
            if self.score == 21 and len(self.hand) == 2:
                print("\n\t________Congratulations! You got a BLACKJACK!________")
                self.money += int (2.5 * self.bet)
            else:
                self.money += 2 * self.bet
        else:
            print("\n\n\t---------Sorry! You Busted! You Lose!---------")
        self.bet = 0

    def draw(self):
        print("\n\n\t---------It's a Draw!----------")
        self.money += self.bet
        self.bet = 0

    def hasBlackJack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False