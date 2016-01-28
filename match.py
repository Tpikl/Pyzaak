#!/usr/bin/python
import random
from ai import AI
from deck import Deck


class Match(object):
    def __init__(self, Player, Computer):
        self.Player = Player
        self.Computer = Computer
        self.Player.id = 0
        self.Computer.id = 1
        self.Player.stand = 0
        self.Computer.stand = 0
        self.Player.score = 0
        self.Computer.score = 0
        self.Player.playedCards = []
        self.Computer.playedCards = []
        self.Player.hand = []
        self.Computer.hand = []
        self.coin = 0
        self.masterDeck = Deck("Deck", True)

    def main(self):
        print("Players: " + self.Player.name + " vs " + self.Computer.name)


        # Draw cards
        self.Player.Deck.drawHand()
        self.coin = random.getrandbits(1)
        self.newRound()

    def newRound(self):
        self.coin = not self.coin
        self.Player.stand = 0
        self.Computer.stand = 0
        self.Player.playedCards = []
        self.Computer.playedCards = []

        if self.coin:
            print("Player's turn")
            self.turn(self.Player)
        else:
            print("Computer's turn")
            self.turn(self.Computer)

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
                self.Computer.playedCards.append(self.masterDeck.drawCard())
                self.Computer.stand = AI.determineAction(self.Computer.score, self.Computer.hand)
            else:
                self.Player.playedCards.append(self.masterDeck.drawCard())
                self.displayPlayedCards()
                self.showHand()

                self.Player.stand = self.displayChoices(0)

        # Turn over - Check for end of round
        if self.Player.stand == 1 and self.Computer.stand == 1:
            self.checkRoundWin(sum(self.Player.playedCards), sum(self.Computer.playedCards))

        # Start next turn
        if self.Player.score < 3 and self.Computer.score < 3:
            if Player.id == 0:
                self.turn(self.Computer)
            else:
                self.turn(self.Player)
        else:
            print("Game Over")
            print("Winner: " + self.Player.name) if (self.Player.score == 3) else print("Winner: " + self.Computer.name)
            input(":")
            from menus import Menus
            M = Menus(self.Player)
            M.menu()

    def displayChoices(self, played):
        if played:
            print("End | Stand\n")
        else:
            print("Play | End | Stand\n")

        playerSelect = input(":").lower()

        if playerSelect == "play" or playerSelect[0] == 'p' and not played:
            return self.playCard()
        elif playerSelect == "end" or playerSelect[0] == 'e':
            return 0
        elif playerSelect == "stand" or playerSelect[0] == 's':
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
            self.Computer.score += 1
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
        print("--" + str(self.Player.score) + "---- " + self.Player.name + " -V- " + self.Computer.name + " ----" + str(
            self.Computer.score) + "--")

    def displayPlayedCards(self):
        print(str(sum(self.Player.playedCards)) + "   |   " + str(sum(self.Computer.playedCards)))
        print(str(self.Player.playedCards) + "-|-" + str(self.Computer.playedCards))
        print("\n")

    def showHand(self):
        print("--Hand-------")
        print(self.Player.Deck.hand)
        print("-----------")
