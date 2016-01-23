#!/usr/bin/python
import os

from deck import Deck


def main():
	intro()
	input("")

	menuSelect = menu()
	
	if menuSelect == '1':
		play()
	elif menuSelect == '2':
		deck()
	elif menuSelect == '0':
		print("Thanks for playing!")
		exit()
	else:
		print("Invalid entry")
		menu()
		
def intro():
	print("Welcome to Pyzaak")
	print("A python Pazaak game")
	print("May the Force be with you.\n")
	
def menu():
	#Print the options
	print("Pazaak Menu")
	print("---------")
	print("1 - Play")x	
	print("2 - Deck")
	print("0 - Exit")
	return input()
	
def deck():
	print("View Deck")
	d = Deck("Test Deck")
	d.listDeck()

def play():
	print("Play!")
	#Create user deck file

	
main()