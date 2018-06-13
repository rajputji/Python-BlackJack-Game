"""
AUTHOR

    Abhishek Rajput <Abhishekrajput676@gmail.com>

"""

import os
from PlayerModule.Players import Player
from Deck import *

def clear():
    if os.name == 'nt':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')

def printDealer(Dealer):
    for i in range(len(Dealer.hand)):
        if i == 0 :
            print("#", end = " ")  #hiding first card of Dealer
        elif i == len(Dealer.hand)-1:
            print(Dealer.hand[i])
        else:
            print(Dealer.hand[i], end = " ")



def main():
    clear()
    print("\n\n\t*****WELCOME TO BLACKJACK******")
    print("\n\tLet's Play!")
    print("\n\tShuffling the Cards....")
    print("\n\n\tPerfectly shuffled!!")
    amt = int(input("\n\n\tEnter initial amount of money you have to play the game : "))

    cardDeck = createDeck()
    firstHand = [cardDeck.pop(),cardDeck.pop()]
    secondHand = [cardDeck.pop(),cardDeck.pop()]
    Player1 = Player(firstHand,amt)
    Dealer = Player(secondHand)
    cardDeck = createDeck()

    while(True):
        if len(cardDeck) < 20 :
            cardDeck = createDeck()
        
        firstHand = [cardDeck.pop(),cardDeck.pop()]
        secondHand = [cardDeck.pop(),cardDeck.pop()]
        Player1.play(firstHand)
        Dealer.play(secondHand)


        print("\n\tYour Hand :\t\t",end = " "),print(Player1)
        print("\n\tDealer is showing :\t",end = " "),printDealer(Dealer)

        Bet = int(input("\n\tEnter your bet : "))
        if Bet <= Player1.money:
            Player1.betMoney(Bet)
        else:
            while Bet > Player1.money:
                print("\n\tNot Enough Money!! You have Rs." + str(Player1.money) )
                print("\n\tTry to bet a little lesser...")
                Bet = int(input("\n\tEnter your bet : "))


        if Player1.hasBlackJack():
            if Dealer.hasBlackJack():
                print("\n\tBoth you and Dealer got a BLACKJACK")
                Player1.draw()
            else:
                Player1.win(True)
        else:
            while(Player1.score < 21 ):
                print()
                action = input("\n\tDo you want another card (i.e. Hit )? (y/n) : ")
                print()
                if action == "y":
                    Player1.hit(cardDeck.pop())
                    print("\n\tYour Hand :\t\t",end = " "),print(Player1)
                    print("\n\tDealer is showing :\t",end = " "),printDealer(Dealer)
                else:
                    break

            while(Dealer.score < 16):
                Dealer.hit(cardDeck.pop())

            print("\n\tYour Hand :\t\t",end = " "),print(Player1)
            print("\n\tDealer's Hand :\t\t",end = " "),print(Dealer)
            
            if Player1.score > 21 :
                if Dealer.score > 21 :
                    Player1.draw()
                else:
                    Player1.win(False)
            elif Player1.score > Dealer.score:
                Player1.win(True)
            elif Player1.score == Dealer.score:
                Player1.draw()
            else:
                if Dealer.score > 21:
                    Player1.win(True)
                else:
                    Player1.win(False)

        print("\n\n\tYour Total Money = " + str(Player1.money))
        
        if Player1.money <= 0 :
            break

        ans =input("\n\tWant to play more? (y/n) :")
        if ans != "y":
            break
        clear()
        print("\n\tLet's play furthur....")


if __name__ == "__main__":
    main()