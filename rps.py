#!/usr/bin/python3

import random

user_wins = 0
comp_wins = 0

def Choice_Options():
	user_choice = input("\nEnter your choice[Rock, Paper, Scissor] : ")
	if user_choice in ["Rock","R","rock","r"]:
		user_choice = "r"
	elif user_choice in ["Paper","P","paper","p"]:
		user_choice = "p"
	elif user_choice in ["Scissor","S","scissor","s"]:
		user_choice = "s"
	else:
		print("I didn't get what you're trying to say please try again.")
		Choice_Options()
	return user_choice

def Computer_Options():
	comp_choice = random.randint(1, 3)
	if comp_choice == 1:
		comp_choice = "r"
	elif comp_choice == 2:
		comp_choice = "p"
	else:
		comp_choice = "s"
	return comp_choice

while True:
	print("")
	user_choice = Choice_Options()
	comp_choice = Computer_Options()
	print("")

	if user_choice == "r":

		if comp_choice == "r":
			print("\nYour choice => Rock")
			print("Computer choice => Rock")
			print("===== It's a tie. =====")

		elif comp_choice == "p":
			print("\nYour choice => Rock")
			print("Computer choice => Paper")
			print("----- You Lose.😭️ -----")
			comp_wins += 1

		else:
			print("\nYour choice => Rock")
			print("Computer choice => Scissor")
			print("+++++ You Win.😎️ +++++")
			user_wins += 1

	elif user_choice == "p":

		if comp_choice == "r":
			print("\nYour choice => Paper")
			print("Computer choice => Rock")
			print("+++++ You win.😎️ +++++")
			user_wins += 1

		elif comp_choice == "p":
			print("\nYour choice => Paper")
			print("Computer choice => Paper")
			print("===== It's a tie. =====")

		else:
			print("\nYour choice => Paper")
			print("computer choice => Scissor")
			print("----- You Lose.😭️ -----")
			comp_wins += 1

	elif user_choice == "s":

		if comp_choice == "r":
			print("\nYour choice => Scissor")
			print("Computer choice => Rock")
			print("----- You Lose.😭️ -----")
			comp_wins += 1

		elif comp_choice == "p":
			print("\nYour choice => Scissor")
			print("Computer choice => Paper")
			print("+++++ You Win.😎️ +++++")
			user_wins += 1

		else:
			print("\nYour choice => Scissor")
			print("Computer choice => Scissor")
			print("===== It's a tie. =====")

	print("")
	print("Your Wins : ",str(user_wins))
	print("Computer Wins : ",str(comp_wins))
	print("")
	cont = input("Do you want to continue.[Yes/No] : ")

	if cont in ["Yes", "Y", "yes", "y"]:
		pass
	
	elif cont in ["No","N","no","n"]:
		
		if user_wins < comp_wins:
			print("\n\t\t\t😭️Computer is the Winner.😭️\n")
		elif user_wins == comp_wins:
			print("\n\t\t\tIt's a tie.\n")
		else:
			print("\n\t\t\t😎️User/You are the Winner.😎️\n")
		break
	
	else:
		
		if user_wins < comp_wins:
			print("\n\t\t\t😭️Computer is the Winner.😭️\n")
		elif user_wins == comp_wins:
			print("\n\t\t\tIt's a tie.\n")
		else:
			print("\n\t\t\t😎️User/You are the Winner.😎️\n")
		break