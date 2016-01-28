#!/usr/bin/python
from match import Match
from ai import AI


class Menus(object):
	def __init__(self, Player):
		self.Player = Player
		
	def menu(self):
		print("Hello " + self.Player.name + "!\n")

		#Print the options
		print("Pazaak Menu")
		print("---------")
		print("Play")
		print("Deck")
		print("How to Play")
		print("Test")
		print("Quit")
		menuSelect = input(":").lower()

		if menuSelect == 'play' or menuSelect[0] == 'p':
			self.match()
		elif menuSelect == 'deck' or menuSelect[0] == 'd':
			self.viewDeck()
		elif menuSelect == 'how to play' or menuSelect[0] == 'h':
			self.howPlay()
		elif menuSelect == 'test' or menuSelect[0] == 't':
			self.test()
		elif menuSelect == 'quit' or menuSelect[0] == 'q':
			print("Thanks for playing!")
			exit()
		else:
			print("Invalid entry")
			self.menu()
	
	def match(self):	
		m = Match(self.Player, AI())
		m.main()

	def viewDeck(self):
		print("View Deck")
		self.Player.Deck.listDeck()

		input(":")
		self.menu()

	def howPlay(self):
		from howPlay import howPlay
		h = howPlay()
		h.howAbout()


	def test(self):
		#I use this to test small snippets of code quickly
		pass