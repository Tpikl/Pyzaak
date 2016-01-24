#!/usr/bin/python
from deck import Deck

class Player(object):
	def __init__(self, name):
		self.name = name
		self.Deck = Deck("Test Deck")
