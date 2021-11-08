vowels = ['a', 'e', 'i', 'o', 'u']

def pig_lat_wrd():

	word = input("enter a wordi: ")
	if(word[0].lower() in vowels and word.isalpha()):
		new_word = word.lower() + "way" 
		print(new_word)
	elif(word.isalpha()):
		new_word = word[1:] + word[0].lower() +'ay'
		print(new_word)
	else:
		print("improper entry")
		pig_lat_wrd()

def pig_sen():
	sen = input("enter sentence: ")
	new_sen = ""
	words = sen.split()
	for word in words:
		if(word[0].lower() in vowels and word.isalpha()):
			new_word = word.lower() + "way"
			print(new_word)
		elif(word.isalpha()):
			new_word = word[1:] + word[0].lower() +'ay'
			print(new_word)
		else:
			print("improper entry")
			pig_sen()
		new_sen = new_sen + new_word + ' '
	new_sen = new_sen[0:-1]
def choices():
	choice = input("Would you like to convert a word or a sentence enter (W/S)? ")
	choice = choice.lower()
	if(choice == 'w'):
		pig_lat_wrd()
	elif(choice == 's'):
		pig_sen()
	else:
		print("Invalid option try again")
		choices()


choices()



