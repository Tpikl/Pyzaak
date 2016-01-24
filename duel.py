#!/usr/bin/python
import os
import random
from ai import AI

class Duel(object):
	def __init__(self, Player, Enemy):
		self.Player = Player
		self.Enemy = Enemy
		self.Player.id = 0
		self.Enemy.id = 1
		self.Player.score = 0
		self.Enemy.score = 0
		self.Player.playedCards = []
		self.Enemy.playedCards = []
		self.Player.hand = []
		self.Enemy.hand = []

	def main(self):
		print("Players: " + self.Player.name + " vs " + self.Enemy.name)

		#Draw cards
		self.drawHands()

		#Decide who is first
		#Wrap rounds around turns - Best 2/3
		if (random.getrandbits(1)):
			print("Player's turn")
			self.turn(self.Player)
		else:
			print("Enemy's turn")
			self.turn(self.Enemy)


	def turn(self, Player):
		#Runs for each turn
		self.clear()
		
		#Display current duel info
		self.displayScores()

		#Handle AI turn if necessary
		if (Player.id == 1):
			self.Enemy.playedCards.append(self.drawCard())
			AI.determineAction(self.Enemy.score, self.Enemy.hand)
		else:
			turn = 1

			self.Player.playedCards.append(self.drawCard())
			self.displayPlayedCards()
			self.showHand()

			while turn:
				print("Play | End | Stand")
				select = input(": ").lower()
				if select == "play":
					index = input("Card Index: ")
					card = self.Player.hand[int(index)] 

					if card != 0:
						self.Player.playedCards.append(card)
						self.Player.hand[int(index)] = 0
						self.displayPlayedCards()
				elif select == "end":
					turn = self.endTurn()
				elif select == "stand":
					self.stand()
				else:
					print("Invalid")

		#Turn over - Start next turn
		if (Player.id == 0):
			self.turn(self.Enemy)
		else:
			self.turn(self.Player)

	def displayScores(self):
		print("--"+ str(self.Player.score) +"---- "+ self.Player.name +" -V- "+ self.Enemy.name +" ----"+ str(self.Enemy.score) +"--")

	def displayPlayedCards(self):
		print(str(self.Player.playedCards) +"--|--"+ str(self.Enemy.playedCards))
		print("\n")


	def showHand(self):
		print("--Hand-------")
		print(self.Player.hand)
		print("-----------")

	def playCard(self):
		#Used to play a card
		return

	def drawHands(self):
		#Draw player's hand of 4 cards
		self.Player.hand = [1,3,-4,5]
		self.Enemy.hand = [1,2,4,-1]
	
	def drawCard(self):
		#Standard draw at the beginning of each player's turn
		return random.randint(1,10)

	def endTurn(self):
		#User 'End Turn' option
		print("--Turn over")
		return 0

	def stand(self):
		#User 'Stand' option
		print("--Standing")
		return 0

	def coinToss(self):
		#Method to decide who goes first.
		#Randomize between the two
		return random.getrandbits(1)

	def clear(self):
		for x in range(0,10):
			print("\n")