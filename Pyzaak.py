#!/usr/bin/python
import os
from menus import Menus

#Start Here!
def main():
	print("Welcome to Pyzaak")
	print("A python Pazaak game")
	print("May the Force be with you.\n")
	print("--------\n")
	print("Please enter your name: ")
	playerName = input()

	M = Menus(playerName)
	M.menu()

main()