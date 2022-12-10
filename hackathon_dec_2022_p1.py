import time
import sys

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
print(numbers)

if numbers != '':
	leaderboard = numbers.split("\n")
	leaderboard.remove('')
	print(leaderboard)
	leaderboard = [int(i) for i in leaderboard]
	f.close()


print(leaderboard)

if len(leaderboard)<5:
	leaderboard = [leaderboard[i] for i in range(0,len(leaderboard))]
else:
	leaderboard = [leaderboard[i] for i in range(0,4)]



def typing_thingy():
	begining = time.time()
	line_to_type = "The quick brown fox jumps over the lazy dog"
	string = input("type:{line}\n".format(line = line_to_type))


	# leaderboard = {"1st":[1],"2nd":[2],"3rd":[3],"4th":[],"5th":[]}
	# print(len(leaderboard))
	

	if string == "E" or string == "e":
		print("Okay! Exiting program!!")
		sys.exit()


	while string != line_to_type:
		string = input("You typed it incorrectly, type again\n{line}\n".format(line = line_to_type))
		if string == "E" or string == "e":
			print("Okay! Exiting program!!")
			sys.exit()



	ending = time.time()
	net_time = ending - begining

	length = len(line_to_type.split())
	wpm = (length/net_time)*60
	wpm = int(wpm)

	# if len(leaderboard)<5:
	# 	leaderboard.append(wpm)
	# else:
	# 	for i in range(0,5):
			
	# 		if wpm < leaderboard[i]:
	# 			if i != 4:
	# 				if leaderboard[i+1] < wpm:
	# 					leaderboard.insert(i+1, wpm)
	valid_indexes = [0,1,2,3,4]
	
	global leaderboard
	leaderboard.append(wpm)
	leaderboard = sorted(leaderboard, reverse = True)

	f = open("leaderboard.txt", "w")

	

	for score in leaderboard:
		f.write(str(score))
		f.write("\n")
	f.close()
	



	print(leaderboard)
	print("your speed was {wpm}wpm".format(wpm = wpm))
	command = input("Type A to try again, L to see leaderboard, or E to exit\n")
	




	if command == "A" or command == "a":
		typing_thingy()
	elif command == "E" or command == "e":
		print("Okay! Exiting program!!")
		sys.exit()
	elif command == "L" or command == "l":
		print([leaderboard[n] for n in valid_indexes if n < len(leaderboard)])

typing_thingy()













