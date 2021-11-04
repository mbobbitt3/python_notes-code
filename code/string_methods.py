#string methods 

'''
startswith()
endswith()
'''
'''
course = "CSI-160"
print(course.startswith("CSI-"))
print(course.endswith("160"))
course_num = [-3:]
print(course_num.isdecimal())
'''
def course_check():
	x = input("enter course num: ")
	x = x.upper()
	csi = x.startswith("CSI-")
	if(csi == False):
		print("invalid course try again")
		course_check()
	else:
		pass
	cnum = x.split('-')
	cnum = cnum[1]
	cnum = int(cnum)

	if(cnum >=100 and cnum <= 499):
		print("that is a valid course")

	else:
		print("that is not a valid course try again")
		course_check()

course_check()
# pass last 3 char to var
#verify cnum is between 100 and 499 inclu
#if true print valid course else print invalid course try again
