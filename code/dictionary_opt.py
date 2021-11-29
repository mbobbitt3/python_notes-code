cit_230 = {'John':89, 'Sue':90, 'Steve':88, 'James':99}
cit_235 = {'Sue':77,'Steve':88, 'John':89}
students = {'name':'John', 'courses':['CIT-230', 'CIT=235'], 'year':1}

students.update({'name':'Sue'})

#del cit_230['John']
yr = students.pop('year') #deletes value stored in key

print("the value of the year deleted was: ", yr)
'''
while True:
	print("Enter a name: (Blank to Quit)")
	name = input()
'''
'''
for v in cit_230.values():
	print("the values are: ", v)
for k in cit_235.keys():
	print("the keys are: ", k)
for key,value in cit_230.items():
	print("For the key", key, "the value equals: ", value)

print("the items in CIT 235 are: ", cit_235.items())

grades = list(cit_235.values())
print(grades)
'''
'''
print("the grade equals: ", str(cit_235.get('John')))
print("the grade equals: ", str(cit_235.get('John', 'Not Found')))

newList = []

for i in range(len(cit_235.items())):
	newList.append(list(cit_235.keys())[i])
	newList.append(list(cit_235.values())[i])

print("the new list contains: ", newList)

#make list into dict
def convert(lst):
	d_f = {lst[i]: lst[i+1] for i in range(0, len(lst), 2)}
	return d_f

lst = ['Paul', 90, 'Matt', 88, 'Mary', 89]
print(convert(lst))

import pprint
message = "A Python programmer is in demand"
count = {}
for char in message:
	count.setdefault(char, 0)
	count[char] = count[char] + 1

pprint.pprint(count)
'''
