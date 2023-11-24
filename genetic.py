from random import *

def make_parents(list1,lth):
    lenth = lth+1
    p1 = [None]*lenth
    p1[0] = list1[0]
    p1[lenth-1] = list1[0]
    for i in range(1,lenth-1):
        while True:
            j = randint(1,lenth-2)
            if list1[j] not in p1:
                p1[i] = list1[j]
                break
    return p1

def mutattion(p1,lth):
    # change values of 3% of actual values
    c = int(len(p1)* 0.03)
    if c < 0:
        c = 1
    for i in range(c):
        a = randint(1,lth-2)
        while True:
            b = randint(1,lth-2)
            if a != b:
                break
        p1[a],p1[b] = p1[b],p1[a]
    
    return p1 
        

def order_croosover(p1,p2,lth):
    a = randint(1,lth-2)
    b = randint(1,lth-2)

    if a > b:
        a,b = b,a
    # print(a,b)
    c1 = [None]*lth
    c1[0] = p1[0]
    c1[lth-1] = p1[0]
    
    c2 = [None]*lth
    c2[0] = p2[0]
    c2[lth-1] = p2[0]
    
    count = 0
    for i in range(a,b+1):
        c1[i] = p1[i]
        c2[i] = p2[i]
        count += 1
    
    # for child 1
    count = lth-count-2
    q = 1
    for i in range(b+1,lth-1):
        if count == 0:
            break
        if q >= lth-1:
            break
        while c1[q] != None and q<lth-2:
            q += 1 
        if q >= lth-1:
            break
        if p2[i] not in c1: 
            c1[q] = p2[i]
            count -= 1
            q += 1
            
    for i in range(1,b+1):
        if count == 0:
            break
        if q >= lth-1:
            break
        while c1[q] != None and q<lth-2:
            q += 1 
        if q >= lth-1:
            break
        if p2[i] not in c1: 
            c1[q] = p2[i]
            count -= 1
            q += 1
    
    # for child 2        
    count = lth-count-2
    q = 1
    for i in range(b+1,lth-1):
        if count == 0:
            break
        if q >= lth-1:
            break
        while c2[q] != None and q<lth-2:
            q += 1 
        if q >= lth-1:
            break
        if p1[i] not in c2: 
            c2[q] = p1[i]
            count -= 1
            q += 1
            
    for i in range(1,b+1):
        if count == 0:
            break
        if q >= lth-1:
            break
        while c2[q] != None and q<lth-2:
            q += 1 
        if q >= lth-1:
            break
        if p1[i] not in c2: 
            c2[q] = p1[i]
            count -= 1
            q += 1
            
        
    return c1,c2
    
def fitness(child):
    
    distance = [[0,1,23,3,4,95],
                [1,0,2,3,45,5],
                [1,2,0,3,4,50],
                [1,92,3,0,44,5],
                [1,2,53,4,0,5],
                [1,2,3,34,25,0]]
    
    total = 0
    for i in range(len(child)-1):
        total += distance[child[i]-1][child[i+1]-1]
    # print(total)
    return total

def genetic(list1):
    total_routes = []                
    lenth = len(list1)
    p1 = make_parents(list1,lenth)
    p2 = make_parents(list1,lenth)
    # print("parents")
    # print(p1)
    # print(p2)
    
    total_routes.append(p1)
    total_routes.append(p2)
    
    count = 10
    while count > 0:
       
        # print("chilren")
        # print(c1)
        # print(c2)
        
        c1,c2 = order_croosover(c1,c2,len(p1))
        
        c1 = mutattion(p1,len(p1))
        c2 = mutattion(p2,len(p2))
        
        # print("chilren")
        # print(c1)
        # print(c2)
        total_routes.append(c1)
        total_routes.append(c2)
        count -= 1
        
    total_routes.sort(key=fitness)
    return total_routes[0]
    
    
if __name__== "__main__":
    list1 = [1,2,3,4,5,6]
    print(f"Optimal path is {genetic(list1)}")
    