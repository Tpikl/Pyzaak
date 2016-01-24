#!/usr/bin/python

class Deck(object):
	def __init__(self, name):
		self.name = name
		self.deck = [1,1,2,2,3,3,4,4,5,5]

	def listDeck(self):
		print("-----")
		print("Deck: " + self.name)
		for card in self.deck:
			print(card)
		print("---")