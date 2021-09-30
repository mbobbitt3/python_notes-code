grades = [10,9,7,9,8,10]
counter = 0
for i in grades:
	if(i == 9):
		counter += 1
		grades.remove(i)
	else:
		pass
print(counter)
print(grades)

grades.insert(1,9) #inser(idx, value)
grades.insert(3,9) #inser(idx, value)
print(grades)
