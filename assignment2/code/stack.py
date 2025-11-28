'''



empty stack [0]

[] stack that contains 3,2,1

3 is the top of the stack



'''

# creates a stack with x

def create(x):

    s=[x]

    return s    



def is_empty(s):

    return s==[]



def insert(s,x):

    s.insert(0,x)

    

def remove(s):

    if is_empty(s): # underflow
        return 0

    x=s[0]

    s.pop(0)

    return x



