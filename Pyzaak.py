#!/usr/bin/python
import os

def main():
	intro()
	input("")
	menuSelect = menu()
	
	if menuSelect == '1':
		#play method here
		print("Play!")
	elif menuSelect == '2':
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
	print("1 - Play")
	print("2 - Exit")
	return input()
	
main()