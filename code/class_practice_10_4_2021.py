import math, random 
#Import the random and math libraries

'''
You will have to write an algorithm that will instruct a programmer to write Python code that will
allow a user to enter a name and programming skill level and then output the results to the output
console in PyCharm. You may write the algorithm using Microsoft Word.

Write Python code that lets a user enter their full name and then choose a mathematical procedure. The procedures
you will set up include calculating the area of a square, the area of a triangle or the area of a circle. Next, given
the procedure the user wishes to perform, ask for the proper inputs to perform the calculation. The are of a circle
equals Pi*the radius squared. The area of square is the length of one of its sides squared. The area of a triangle
equals .05*base*height. Be sure you provide the proper output so that the users gets an answer.

Write Python code that randomly generates a number between 1 and 10. Then give the user a chance to guess the number.
If the user is right, output a response that informs the user of the correct guess. If the user is wrong, tell the
user it was a wrong guess and tell them the answer.

CHALLENGE EXERCISE:
Expand the guessing game to allow the user three chances to guess the number. Also, if the user makes a wrong guess,
tell the user to guess higher or lower depending on thier guess. For example, if the number is 6 and the user
guesses 4, tell the user to guess higher.
'''



def math_proc():
	name = input("What is your name ")
	proc = input("please select an operaion: area square, area triangle, area circle ")

	if(proc == "area square"):
		side =  float(input("enter length of side of square "))
		square =  side ** 2
		print("the area of your square is:", square, "square units")
	elif(proc == "area triangle"):
		base =  float(input("enter base length of triangle: "))
		height = float(input("enter the height of the triangle: "))
		triangle =  (0.5) * (base  * height)
		print("Area of triangle is", triangle, "square units")

	elif(proc == "area circle"):
		radius = float(input("enter radius of circle: "))
		circle =  math.pi * radius ** 2
		print("area of circle is: ", circle, "square units")

	else:
		print("invalid option try again")
		math_proc()

math_proc()
