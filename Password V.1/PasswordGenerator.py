def passwordgenerator():
	try:
		
		#imports
		#really it's just random module
		
		from random import shuffle, randint
		
		#create all the variables
		#a """*pretend there's an enter here*""" randomly is horrible code, so why not turn it into a variable
		
		enter = """
		"""
		password = []
		characters = [
		 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
		 "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
		 "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
		 "T", "T", "V", "W", "X", "Y", "Z","0", "1", "2", "3", "4", "5", "6", "7", 
		 "8", "9"
		]
		
		#all the required input
		
		numchar = input("how much characters do you want? >>> ")
		username = input("what's the accompanying username? >>> ")
		
		#makes the amount of letters and numbers that the user selected
		
		for i in range(0, int(characters)):
			shuffle(characters)
			b = letters[randint(0, len(characters) - 1)]
			password.append(b)
			
		#makes it more random
			
		shuffle(password)
		
		#turns password into a string
		
		Password = ''.join(password)
		with open('Pythonstorage.txt', "a") as myfile:
			myfile.write("Username: " + str(username) + " Password: " + str(Password) + enter)
		print(Password)
	except Exception as E:
		
		#just in case ;)
		
		print("sorry, something went wrong: " + str(E))
	finally:
		
		#ALWAYS CLOSE THE FILE AFTER YOU'RE DONE!
		
		myfile.close()

		#actually runs the file, made this mistake before.
passwordgenerator()
