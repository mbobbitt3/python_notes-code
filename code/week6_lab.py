










#solution to 5
def listing():
	items=[]
	num_iter = int(input("how many items would yoy like to add to the list: "))
	for i in range(num_iter):
		newWord = input("Enter a word to add to the list (press return to stop adding words): ")
		if newWord == "":
			break
		else:
			items.append(newWord)

	items.insert(num_iter-1, "and")
	for i in len(items):
		if(i == num_iter):
			print(i, end =' ')
listing()
