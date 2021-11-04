var = "this is a variable that holds string data"

num = 6271372137219
num = str(num)


num = (', '.join(num))
val = []
for i in num:
	if(i.isdecimal()):
		i = int(i)
		val.append(i)
	else:
		pass
print("the list \'val\' equals: ",val)
print(val[0])
