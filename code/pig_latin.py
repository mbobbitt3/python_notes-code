vowels = ['a', 'e', 'i', 'o', 'u']

def pig_latin():

	word = input("enter a wordi: ")
	if(word[0].lower() in vowels and word.isalpha()):
		new_word = word.lower() + "way" 
		print(new_word)
	elif(word.isalpha()):
		new_word = word[1:] + word[0].lower() +'ay'
		print(new_word)
	else:
		print("improper entry")
		pig_latin()

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

pig_sen()
