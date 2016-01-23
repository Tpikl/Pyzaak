#!/usr/bin/python
import os

class Duel(object):
	def __init__(self, playerOne, playerTwo):
		self.playerOne = playerOne
		self.playerTwo = playerTwo

	def play(self):
		p1 = str(self.playerOne)
		p2 = str(self.playerTwo)
		print("Players: " + p1 + " vs " + p2)

	def playCard():
		#Used to play a card
		return

	def drawHand():
		#Draw player's hand of 4 cards
		return
	
	def drawCard():
		#Standard draw at the beginning of each player's turn
		return

	def endTurn():
		#User 'End Turn' option
		return

	def stand():
		#User 'Stand' option
		return

	def coinToss():
		#Method to decide who goes first.
		#Randomize between the two
		return
