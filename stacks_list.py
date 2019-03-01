#create a stack and a few operations
from sys import maxsize 

def createStack():
    stack = []
    return stack
    
def isEmpty(stack):
    return len(stack)==0

def push(stack, item):
    stack = stack.append(item)
    return stack
    
def pop(stack):
    if (isEmpty(stack)):
         return str(-maxsize -1)
    return stack.pop()
    
#driver code 
stack = createStack()
push(stack, str(10))
push(stack, str(15))
push(stack, str(100))

print(stack)
print(pop(stack)) 
print(stack)
