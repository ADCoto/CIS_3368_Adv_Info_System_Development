# 01/245/2023
# Going to start of teaching us the back end of a database to better understand how the front end and backend work together.
# Reviewing basic python concepts
"""
value = input('Please type some string.\n')
value2 = 'Hello'

print(value)
print('You have entered string as:', value)

print(value2, value)
print('You have entered string as:', value2, value)
print('You have entered string as:'+ value)
print(f'You have entered string as: {value}')
"""

# Data Structure such as List, Dictionary, Tuple and Sets

# Dictionaries
'''
myDict = {
    'firstName' : 'John',
    'lastName' : 'Doe',
    'age' : 24,

    # Nested Dicitonary within another dictionary
    'studentDict' : {
        'studentID' : 123,
        'userName' : 'abc',
        'college' : 'COT'
    },

    # nested list within a dictionary
    'classList' : ['CIS 3368', 'CIS 3365', 'CIS3347']
}

print(len(myDict))
print(myDict.keys())
print(myDict.values())
print(myDict)
print(myDict['firstName'])
print('Hello, this is {} {} my age is {}.'.format(myDict['firstName'], myDict['lastName'], myDict['age']))

print(myDict['studentDict'])
print(myDict['classList'])

myDict['age'] = 25

print(myDict)

# built-in functions : getting values form the dictionary
age = myDict.get('age')

print(age)
print(myDict.get('lastName'))

# update values to the dictionary 
myDict.update({'lastName' : 'Dick'})
print(myDict)

myDict['fName'] = 'F John'
print(myDict)

# Deleting values form the dictionary
myDict.pop('fName')
print(myDict)

del myDict['age']
print(myDict)

myDict.clear()
print(myDict)
'''
'''
del myDict
print(myDict)
This causes an error because it is trying to call apon a dict that no longer exist because 'del myDict' delets the whole variable
unlike myDict.clear which only deletes the data within the variable leaving the variable to still exist.
'''

# List -  it is a collection which is in order and changeble. Allows duplicate valuues.
myList = [1, 2, 5, 5, 8, 9, 7, 6, 3, 4, 6, 7, 8, 9]

myList2 = ['apples', 'oranges', 'mangos', 'peaches', 'kiwi', 'mango']

myList3 = [True, False, False, True, True]

myList4 = ['Kiwi', 123, True, 'Mango', 456, False]

print(myList)
print(myList2)
print(myList3)
print(myList4)

print(myList[3]) # single item from the list
print(myList[1:4]) # range of items form the list
print(myList[-1]) # calls the list item fromt the list
print(myList[-3:]) # calls for the last 3 items for the list
print(myList[:3]) # calls for the first 3 items for the list

# Updating the list of items
myList[3] = 'Kiwi' # single value update
print(myList)

myList[1:3] = ['100', False] # range of values update
print(myList)
