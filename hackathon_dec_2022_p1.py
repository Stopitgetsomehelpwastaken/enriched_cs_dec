import time
import sys
from random_word_gen import random_word_generator


try: 
	f = open("leaderboard.txt", "r")
	f.close()
except:
	f = open("leaderboard.txt", "x")



f = open("leaderboard.txt", "r")
leaderboard = []
# for i in f.readlines():
# 	leaderboard.append(i)
numbers = f.read()


if numbers != '':
	leaderboard = numbers.split("\n")
	leaderboard.remove('')
	
	leaderboard = [int(i) for i in leaderboard]
	f.close()





if len(leaderboard)<5:
	leaderboard = [leaderboard[i] for i in range(0,len(leaderboard))]
else:
	leaderboard = [leaderboard[i] for i in range(0,4)]








def commands(command):
	if command == "A" or command == "a":
		typing_thingy()
	elif command == "E" or command == "e":
		print("Okay! Exiting program!!")
		sys.exit()
	elif command == "L" or command == "l":
		print("\n")
		print("Top 5 WPMs:")
		for num in leaderboard:
			print("{num}wpm".format(num = num))
		print("\n")
		command = input("\nType A to try again, L to see leaderboard, E to exit, or stats to see some statistics\n")
		commands(command)
	


def typing_thingy():
	
	# sentence_len = input("\nHow many words would you like to type\n")

	# while int(sentence_len)>30:
	# 	sentence_len = input("too many words, max word count is 30\n")

	# line_to_type = ' '.join(random_word_generator(int(sentence_len)))
	begining = time.time()
	line_to_type = "The quick brown fox jumps over the lazy dog"
	string = input("type:{line}\n".format(line = line_to_type))


	if string == "E" or string == "e":
		print("Okay! Exiting program!!")
		sys.exit()


	while string != line_to_type:
		if string.lower() == line_to_type:
			string = input("You typed it incorrectly.(remember it is case sensitive)")
		string = input("You typed it incorrectly, type again\n{line}\n".format(line = line_to_type))
		if string == "E" or string == "e":
			print("Okay! Exiting program!!")
			sys.exit()

	ending = time.time()
	net_time = int(ending - begining)

	length = len(line_to_type.split())
	wpm = (length/net_time)*60
	wpm = int(wpm)

	
	valid_indexes = [0,1,2,3,4]
	
	global leaderboard

	leaderboard.append(wpm)
	leaderboard = sorted(leaderboard, reverse = True)
	leaderboard_new = []
	for x in leaderboard:
		if leaderboard.index(x) in valid_indexes:
			leaderboard_new.append(x)
	leaderboard = leaderboard_new
	f = open("leaderboard.txt", "w")

	for score in leaderboard:
		f.write(str(score))
		f.write("\n")
	f.close()





	print("\nyour speed was {wpm}wpm".format(wpm = wpm))
	
	
	

	command = input("\nType A to try again, L to see leaderboard, E to exit\n")
	commands(command)

typing_thingy()













