#!/usr/bin/python
import os
from menus import Menus
from player import Player

#Start Here!
def main():
	print("Welcome to Pyzaak")
	print("A python Pazaak game")
	print("May the Force be with you.\n")
	print("--------\n")
	playerName = input("Please enter your name: ")
	print("\n\n\n\n\n")

	P = Player(playerName)
	M = Menus(P)
	M.menu()

main()