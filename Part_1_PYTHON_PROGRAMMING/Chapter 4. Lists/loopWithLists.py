"""
catNames = []
while True:
    print('Enter the name of cat' + str(len(catNames)+ 1 ) + '(or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are:')
for name in catNames:
    print(''+name)
"""


# Using for Loops with Lists
"""
for i in range(4):
    print(i)
    
for i in [0,1,2,3,4]:
    print(i)


supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
 print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
"""

# The in and not in Operators
"""
'howdy' in ['hello', 'hi', 'howdy', 'heyas']

spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
 print('I do not have a pet named ' + name)
else:
 print(name + ' is my pet.')
"""

# The Multiple Assignment Trick
"""
cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
"""

# Using the enumerate() Function with Lists
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
 print('Index ' + str(index) + ' in supplies is: ' + item)