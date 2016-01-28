#!/usr/bin/python
import random
from ai import AI
from deck import Deck


class Match(object):
    def __init__(self, Player, Enemy):
        self.Player = Player
        self.Enemy = Enemy
        self.Player.id = 0
        self.Enemy.id = 1
        self.Player.stand = 0
        self.Enemy.stand = 0
        self.Player.score = 0
        self.Enemy.score = 0
        self.Player.playedCards = []
        self.Enemy.playedCards = []
        self.Player.hand = []
        self.Enemy.hand = []
        self.coin = 0
        self.masterDeck = Deck("Deck", True)

    def main(self):
        print("Players: " + self.Player.name + " vs " + self.Enemy.name)


        # Draw cards
        self.drawHands()
        self.coin = random.getrandbits(1)
        self.newRound()

    def newRound(self):
        self.coin = not self.coin
        self.Player.stand = 0
        self.Enemy.stand = 0
        self.Player.playedCards = []
        self.Enemy.playedCards = []

        if self.coin:
            print("Player's turn")
            self.turn(self.Player)
        else:
            print("Enemy's turn")
            self.turn(self.Enemy)

    def turn(self, Player):
        # Runs for each turn

        # Display current match info
        self.displayScores()
        # Apart of the drawCard phase


        if Player.stand == 1:
            pass
        else:
            if Player.id == 1:
                # Handle AI turn if necessary
                self.Enemy.playedCards.append(self.masterDeck.drawCard())
                self.Enemy.stand = AI.determineAction(self.Enemy.score, self.Enemy.hand)
            else:
                self.Player.playedCards.append(self.masterDeck.drawCard())
                self.displayPlayedCards()
                self.showHand()

                self.Player.stand = self.displayChoices(0)

        # Turn over - Check for end of round
        if self.Player.stand == 1 and self.Enemy.stand == 1:
            self.checkRoundWin(sum(self.Player.playedCards), sum(self.Enemy.playedCards))

        # Start next turn
        if self.Player.score < 3 and self.Enemy.score < 3:
            if Player.id == 0:
                self.turn(self.Enemy)
            else:
                self.turn(self.Player)
        else:
            print("Game Over")
            print("Winner: " + self.Player.name) if (self.Player.score == 3) else print("Winner: " + self.Enemy.name)
            input(":")
            from menus import Menus
            M = Menus(self.Player)
            M.menu()

    def displayChoices(self, played):
        if played:
            print("End | Stand\n")
        else:
            print("Play | End | Stand\n")

        select = input(":").lower()
        if select == "play" and not played:
            return self.playCard()
        elif select == "end":
            return 0
        elif select == "stand":
            return 1
        else:
            print("Invalid")
            self.displayChoices(played)

    def checkRoundWin(self, playerTotal, enemyTotal):
        if playerTotal == 20 and enemyTotal == 20:
            print("Draw!")
        elif (playerTotal <= 20 and enemyTotal > 20) or (playerTotal <= 20 and enemyTotal < playerTotal):
            self.Player.score += 1
        elif (enemyTotal <= 20 and playerTotal > 20) or (enemyTotal <= 20 and playerTotal < enemyTotal):
            self.Enemy.score += 1
        else:
            print("idk, deal with this if it happens..")

        self.newRound()

    def playCard(self):
        # Used to play a card
        index = input("Card Index:")
        card = self.Player.hand[int(index)]

        if card != 0:
            self.Player.playedCards.append(card)
            self.Player.hand[int(index)] = 0
            self.displayPlayedCards()

            return self.displayChoices(1)
        else:
            print("Invalid selection")
            self.playCard()

    def displayScores(self):
        print("--" + str(self.Player.score) + "---- " + self.Player.name + " -V- " + self.Enemy.name + " ----" + str(
            self.Enemy.score) + "--")

    def displayPlayedCards(self):
        print(str(sum(self.Player.playedCards)) + "   |   " + str(sum(self.Enemy.playedCards)))
        print(str(self.Player.playedCards) + "-|-" + str(self.Enemy.playedCards))
        print("\n")

    def drawHands(self):
        # Draw player's hand of 4 cards
        self.Player.hand = [1, 3, -4, 5]
        self.Enemy.hand = [1, 2, 4, -1]

    def showHand(self):
        print("--Hand-------")
        print(self.Player.hand)
        print("-----------")
