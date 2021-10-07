#find zeroes in list
y = [0, 0 ,0 , 3, 4, 5, 60, 420, 303, 0 , 19032, 20, 30, 0, 10, 0]
idx = 0
count = 0

while(idx < len(y)):
	if y[idx] == 0:
		count += 1
		idx += 1
	else:
		idx += 1

print("number of zeroes found: ", count)
