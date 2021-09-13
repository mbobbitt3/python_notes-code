#working with function
#use 'def' keyword followed by functions name and parantheses

def add_numbers():
    num1 = int(input("enter a number "))
    num2 = int(input("enter a second number: "))
    result = num1 + num2
    print(result)
	make_choice()
def mult_numbers():
    num3 = int(input("enter a number "))
    num4 = int(input("enter a second number: "))
    result1 = num1 * num2
	print(result1)
	make_choice()
#when calling a function use the name and '()'

def make_choice():
    name = input("what is your name? ")
    print("Hello ", name, "pick an optionsi ")
    choice = input("What math operation would you like to do + or * or quit (q)")

    if(choice == '+'):
        add_numbers()

    elif(choice == '*'):
        mult_numbers()
	elif(choice == 'q')
		exit()
	else:
        print("invalid option")
		make_choice()
