'''
# יוצר מחסנית ״משוכללת״
[stack, max. depth, init. state, try next level?]
stack - a simple stack as defined at stack.py
max.depth - the current search depth of ID
init.state - the initial state of the problem
try next level - is there a reason to search deeper
'''
import stack
import state

def create(initial):
    s=stack.create(initial)
    return {"stack":s,"depth":1,"initial":initial,"cutoff":False}

def is_empty(s):
    return stack.is_empty(s["stack"]) and not s["cutoff"] # stack is empty and try next level is false

def insert(s,x):
    if x.path_len()<=s["depth"]: # check if x is not too deep
        stack.insert(s["stack"],x)    # insert x to stack
    else:
        s["cutoff"]=True               # there is a reason to search deeper if needed
    
def remove(s):
    if stack.is_empty(s["stack"]):    # check is there are no states in the stack
        if s["cutoff"]:                # check if there is a reason to search deeper
            s["depth"]+=1             # increase search depth
            s["cutoff"]=False          # meanwhile there is no evidence to  a need to search deeper
            return s["initial"]         # return the initial state
        else:
            return 0
    return stack.remove(s["stack"])   # if there are items in the stack ...

    
