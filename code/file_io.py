#read, write, append file
from os.path  import exists

file_exist = exists('read.txt')

if file_exist == True:
	fd = open('read.txt', 'w')
	name = input("Enter your name: ")
	fd.write(name)
	fd.close()
else:
	fd = open('read.txt', 'a+')
	name = input("Enter name: ")
	fd.write('\n')
	fd.write(name)
	fd.close()

fd = open('read.txt', 'r')
value = fd.read()
print(value)
fd.close()
