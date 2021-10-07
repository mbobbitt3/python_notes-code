import re
def number_of_zeros(grades):
    """Given a list of grades, determines the number of grades that are 0%
    
    params:
    grades (list of floats) - The grades to search. Example [75, 82.5, 97, 0, 87.5]

    return (int) - the number of 0% grades
    """
    zeroes = []
    for i in range(len(grades)):
        if(grades[i] == 0):
            zeroes.append(i) 

    return len(zeroes)
    pass

def median(numbers):
    """Find the median of the given list of numbers.  

    How to find the median:
    https://www.mathsisfun.com/median.html

    Note: Write your own implementation and do not use any libraries.  You will need to sort the list.
    
    params:
    numbers (list) A list containing either int or float elements

    return (numeric) The median value as either an int or float
    """
    numbers.sort()
    mid = len(numbers) // 2
    rc = (numbers[mid] + numbers[~mid]) / 2 # ~ operator here is logical not operator ~i = i-1
    
    return rc
    pass


def top_quartile(grades):
    """Return the top 25% of the grades in the supplied list of grades. Round up when determining how many grades to include in the top 25%.
    
    Hint: You will need to sort the list of grades
    
    params:
    grades (list of floats) Example [75, 82.5, 97, 0, 87.5]
    
    return (list of floats) - The top 25%
    """
    ''''
    top_quart = []
    grades.sort()
    for i in range(len(grades)):
        if(math.ceil(grades[i]) > ):
            top_quart.append(grades[i])
    print(top_quart)
    return top_quart
    '''
    pass

def domain_name_extractor(url):
    """Given a url, return the domain name
    
    You will need to utilize the .find method to complete this https://docs.python.org/3/library/stdtypes.html#str.find

    Hint: Find the starting point of the domain name, then find the end point.
    params:
    url (string) the url to search. Example: https://docs.python.org/3/library

    return (string) The domain name or IP address. Example: docs.python.org
    """
    return url.split("www.")[-1].split("//")[-1].split(".")[0]
    pass

def test_number_of_zeros():
    print('Running number_of_zeros tests:')
    print('Test 1 passed -', number_of_zeros([75.0, 0.0, 97.0, 0.0, 87.5]) == 2)
    print('Test 2 passed -', number_of_zeros([]) == 0)

def test_median():
    print('Running median tests:')
    print('Test 1 passed -', median([10, 5, 8, 4, -1]) == 5)
    print('Test 2 passed -', median([10, 8, 4, -1]) == 6)

def test_top_quartile():
    print('Running top_quartile tests:')
    print('Test 1 passed -', top_quartile([97, 92.5, 84, 79, 67]) == [92.5, 97])
    print('Test 2 passed -', top_quartile([92.5, 86, 89, 75]) == [92.5])

def test_domain_name_extractor():
    print('Running domain_name_extractor tests:')
    print('Test 1 passed -', domain_name_extractor('https://champlain.instructure.com/courses/8933') == 'champlain.instructure.com')
    print('Test 2 passed -', domain_name_extractor('ftp://champlain.edu/myfile.pdf') == 'champlain.edu')

print('Running Unit Tests\n')
test_number_of_zeros()
print()
test_median()
print()
test_top_quartile()
print()
test_domain_name_extractor()

