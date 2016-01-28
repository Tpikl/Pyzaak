#!/usr/bin/python
import random
class Deck(object):
	def __init__(self, name, masterDeck):
		self.name = name
		if masterDeck:
			#AI deck
			self.deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10]
			random.shuffle(self.deck)
			self.hand = []
		else:
			#Player side deck
			self.deck = [1,2,3,4,5,1,2,3,4,5]
			random.shuffle(self.deck)
			self.hand = []
#hi


	def listDeck(self):
		print("-----")
		print("Deck: " + self.name)
		for card in self.deck:
			print(card)
		print("---")

#poop
	def drawCard(self):
		drawnCard = self.deck.pop()
		return drawnCard

	def drawHand(self):
		for hand in range(4):
			self.hand.append(self.deck.pop())
