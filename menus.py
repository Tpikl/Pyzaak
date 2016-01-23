#!/usr/bin/python
import os

from duel import Duel
from deck import Deck

class Menus(object):
	def __init__(self, Name):
		self.Name = Name
		
	def menu(self):
		#Print the options
		print("Pazaak Menu")
		print("---------")
		print("1 - Play")
		print("2 - Deck")
		print("0 - Exit")
		menuSelect = input()

		if menuSelect == '1':
			d = Duel(1, 2)
			d.play()
		elif menuSelect == '2':
			self.viewDeck()
		elif menuSelect == '0':
			print("Thanks for playing!")
			exit()
		else:
			print("Invalid entry")
			self.menu()
		
	def viewDeck(self):
		print("View Deck")
		d = Deck("Test Deck")
		d.listDeck()

		input()
		self.menu()