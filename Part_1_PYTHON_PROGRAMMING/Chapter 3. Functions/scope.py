# Scope
# Local Variables Cannot Be Used in the Global Scope
def spam():
    eggs = 31337
    
spam()
eggs = 42
# print(eggs)


# Local Scopes Cannot Use Variables in Other Local Scopes
def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
    print(ham)
# spam()


# Global Variables Can Be Read from a Local Scope
# def spam():
#  print(eggs)
# eggs = 42
# spam()
# print(eggs)


# Local and Global Variables with the Same Name
def spam():
    eggs = 'spam local'
    print(eggs)  # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)  # prints 'bacon local'

eggs = 'global'   # global variable

spam()             # call spam()
print(eggs)        # prints 'global'

bacon()            # call bacon()
print(eggs)        # prints 'global'



# The global Statement
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)