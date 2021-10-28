#print("somewhere \"big boolin\"")



message = "hello world"
x = ''
y = ''
x = message[:5]
y = message[6:]

#print(x, y)
'''
any string we work  with will not begin iwth a spcace.
it will always begin with a num | letter
'''

sen = "I hope u figure this out."
x1 = ''
x2 = ''
x3 = ''
x4 = ''
x5 = ''
x6 = ''
print(len(sen))
for i in range(len(sen)):
	if(ord(sen[0]) == 32):
		break
	else:
		start = i
		print(start)




