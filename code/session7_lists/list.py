grades = [10,9,7,9,8,10]
letters = ['T', 'h', 'i', 's']
mix = [1,'R',-2,'a',True]

#length of list: grades
print(len(grades))

#extract number 7 from grades
print(grades[2])
print(grades[3])

#add elements to a list
grades.append(6) #append always adds to end of list
print(grades)
'''
del grades #this blows away the entire list in memory when this executes list and all references to list in question is gone
grades = [] #reinitializes the list in memory
grades.append(13) #populates reinitialized list
print(grades)
'''
grades.remove(9) #allows for removal of certain elements from a list non recursively
print(grades)
grades.remove(grades[3])
print(grades)

y=grades[1]
grades.remove(y)
print(grades)
