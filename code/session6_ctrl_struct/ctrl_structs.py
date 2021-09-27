import math

#parameters and placeholders
'''
def get_numbers():
	x= int(input("enter first number"))
	y= int(input("enter second number"))
	some_func(x, y)

def some_func(x, y):
	a = x
	b = y
	z = x+y
	print("the value of a = ", str(a))
	print("the value of b = ", str(b))
	print(z)


get_numbers()
'''
'''
x = True
y = False

if(x == True) or (y != False):
	print("faxual")
else:
	print("Capual")
'''

def logic_stuff():
	x = True
	y= False
	name='John'
	if(name != "john") or  (x== True) and (y != False):
		print("The if statement does not fail")
	else:
		print("the if statement failed")


logic_stuff()
