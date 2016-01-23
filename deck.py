#!/usr/bin/python
import os

class Deck(object):
	def __init__(self, name):
		self.name = name
		self.deck = [1,1,2,2,3,3,4,4,5,5]

	def listDeck(self):
		deck = self.deck

		print("-----")
		print("Deck: " + self.name)
		for card in deck:
			print(card)
		print("---")