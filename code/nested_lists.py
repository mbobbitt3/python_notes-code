def main():
	students = [
		['John', 85, 'm',90],
		['Lee', 85, 91, 'm'],
		['Alex', 89, 89,'m', 95 ]
	]
	temp_list = students[0]
	counter = 1
	for i in students:
		for j in i:
			if (isinstance(j, str) and j != 'm'):
				print('\n')
				print("Name: ", j)
				counter = 1
			else:
				print("Exam: ", counter, j)
				counter += 1

main()




'''
for i in range(len(temp_list)):
	print("Name: ", temp_list[i])
	i+=1
	print("EX1: ", temp_list[i])
	print("EX2: ")
'''
