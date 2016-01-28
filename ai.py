#!/usr/bin/python
from deck import Deck

class AI(object):
	def __init__(self):
		self.name = "AI"
		self.Deck = Deck("AI-Deck", True)
	
	def determineAction(self, score, *hand):
		#Handle it in here somehow
		print("-Enemy Stands-")
		return 1

	def chooseCard(self, score, *hand):
		#If AI chooses to play a card, determine which card is best here
		print("Choose card")
		print(hand)