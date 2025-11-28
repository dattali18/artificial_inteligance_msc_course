'''
implements a priority queue using a minimum heap
the heap is represented by a list
the parent of index i is in index (i-1)//2
the left child of index i is in index 2i+1
the right side of index i is in index 2i+2
'''
import state

        
    
    
def create(s, f):
    return {"queue":[s], "function":f,"total":1,"max":1}      # returns a priority queue that contains s

def is_empty(f):
    return f["queue"]==[]    # returns true iff f is empty list

def parent(i):
    return (i+1) //2 - 1 

def leftSon(i):
    return (i+1)*2 - 1

def rightSon(i):
    return (i+1) *2 

def swap(l,x,y):
    t=l[x]
    l[x]=l[y]
    l[y]=t

def insert(pq, s):
    
    # inserts state s to the frontier
    f=pq["queue"]
    val=pq["function"]
    f.append(s)     # inserts the new state as the last item
    i=len(f)-1      # i gets its value
    pq["total"]=pq["total"]+1
    
       
    # move the item with smallest value to the root
    while i>0 and val(f[i]) < val(f[parent(i)]): # while item i's value is smaller than the value of his father, swap!
        # the next three lines swap i and his father
        swap(f, i, parent(i))
        i=parent(i)

def remove(pq):      # remove and return the root of f
    f=pq["queue"]
    m=pq["max"]
    if is_empty(pq): # underflow
        return 0
    if len(f)>m:
        pq["max"]=len(f)
    s=f[0]          # store the root that should be returned
    f[0]=f[len(f)-1]    # the last leaf becomes the root
    del f[-1]       # delete the last leaf
    heapify(pq,0)    # fixing the heap
    return s

 
'''
for greedy best first search val returns hdistance
for uniform cost val returns path len

'''

def heapify(pq,i):   # fix the heap by rolling down from index i
    # compares f[i] with its children
    # if f[i] is bigger than at least one of its children
    # f[i] and its smallest child are swapped
    minSon=i    # define i as minSon
    val=pq["function"]
    f=pq["queue"]
    if leftSon(i)<len(f) and val(f[leftSon(i)])<val(f[minSon]):   # if f[i] has a left son
                                        # and its left son is smaller than f[i]
        minSon=leftSon(i)                    # define the left son as minSon
    if rightSon(i)<len(f) and val(f[rightSon(i)])<val(f[minSon]):   # if f[i] has a right son
                                        # and its right son is smaller than f[minSon]
        minSon=rightSon(i)                    # define the right son as minSon
    if minSon!=i:                       # if f[i] is bigger than one of its sons
        swap(f,i,minSon)
        heapify(pq,  minSon)              # repeat recursively
        
        
    
