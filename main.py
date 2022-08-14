#import otherfile.py
import random
import collections

code_colors = ['red', 'yellow', 'green', 'blue', 'white', 'black']

random_colors = random.sample(code_colors, 4)

# number_of_pegs = len(random_colors) testing that the number of random colors is exactly 4

#print(random_colors) UNCOMMENT THESE FOR TESTING!!
#print(number_of_pegs) UNCOMMENT THESE FOR TESTING!!


print("\nWelcome to Mastermind! 4 colored pegs have been chosen in a random order. The four code colors have been picked out from this group of six: red, blue, yellow, green, black, and white.")
print("\nTry to guess the code (color AND position) in 10 tries! Please note that there are no duplicates. \nSeparate each color with a space. Lower case, please!")
print("\nFor example, a code could look like this: black red blue white")
print("\nEnter your guess here: ")


def string_to_list(string):
	new_list = list(string.split(" "))
	return new_list


#def evaluate_color(user_guess, random_colors):
#	correct_colors = 0
#	for x,y in zip(user_guess,random_colors):
#		if user_guess == random_colors:
#			correct_colors +=1
#			print(correct_colors + " colors are correct!")
		

#def evaluate_position():
	

#bool(codebreaker)


for x in range(10):
	correct_colors = 0
	correct_positions = 0
	user_guess = string_to_list(input("\n"))
	if user_guess!= random_colors:
			print("\nYou guessed:\n\n" + str(user_guess))
			correct_colors = set(random_colors).intersection(user_guess)
			number_of_correct_colors = str((len(list(correct_colors))))
			print("\nNot quite! Here's a hint:")
			if len(correct_colors) == 1:
				print(number_of_correct_colors + " color is correct.")
			elif len(correct_colors) > 1:
				print(number_of_correct_colors + " colors are correct.")
			correct_positions = sum(a == b for a,b in zip(user_guess,random_colors))
			if correct_positions == 1:
				print(str(correct_positions) + " position is correct.")
			elif correct_positions > 1: 
				print(str(correct_positions) + " positions are correct.")
	else:
		print("\nCongratulations! You guessed the code!")
		break


		
	
if user_guess == random_colors:
	print("Wow, you're a codebreaker extraordinnaire!")
else:
	print("\nSorry, you lose. Better luck next time!")




#if user_guess[0] == random_colors[0]:
#			correct_colors +=1
#		if user_guess[1] == random_colors[1]:
#			correct_colors +=1
#		if user_guess[2] == random_colors[2]:
#			correct_colors +=1
#		if user_guess[3] == random_colors[3]:
#			correct_colors +=1


#if correct_colors == 1:
				#print(correct_colors + " color is correct.")
			#elif correct_colors >= 2:
				#print(correct_colors + " colors are correct.")