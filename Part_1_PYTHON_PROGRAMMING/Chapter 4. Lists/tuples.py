# Tuples are typed with parentheses ().
# Tuples values are immutable.

t = (1 ,)
print(type(t))  # type check


print(id(t))

# Passing References
def eggs(someParameter):
 someParameter.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)