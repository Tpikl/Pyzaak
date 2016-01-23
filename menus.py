#!/usr/bin/python
import os

from duel import Duel
from ai import AI

class Menus(object):
	def __init__(self, Player):
		self.Player = Player
		
	def menu(self):
		print("Hello " + self.Player.name + "!\n")

		#Print the options
		print("Pazaak Menu")
		print("---------")
		print("1 - Play")
		print("2 - Deck")
		print("0 - Exit")
		menuSelect = input(": ")

		if menuSelect == '1':
			self.duel()
		elif menuSelect == '2':
			self.viewDeck()
		elif menuSelect == '0':
			print("Thanks for playing!")
			exit()
		else:
			print("Invalid entry")
			self.menu()
	
	def duel(self):	
		d = Duel(self.Player, AI())
		d.main()
	
	def viewDeck(self):
		print("View Deck")
		self.Player.Deck.listDeck()

		input(":")
		self.menu()