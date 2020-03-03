import random

V=5
edges = [0] * V
for i in range(V):
    edges[i]={}

def heuristicFunction(list):
    HVal=0
    for i in range(V-1):
        HVal+=edges[list[i]][list[i+1]]
    return HVal

def swap(list,i,j):
    list[i],list[j]=list[j],list[i]
    return list

def hillClimb():
    current=[]
    while(len(current)<V):
        num = random.randint(0,V-1)
        if num not in current:
            current.append(num)
    print(current)
    HVal = HValtemp = heuristicFunction(current)
    print(HVal)
    while(1):
        neighbor = {}
        tempList = []
        for i in range(V-1):
            for j in range(i+1,V):
                nextList=current.copy()
                swap(nextList,i,j)
                tempVal=heuristicFunction(nextList)
                neighbor[tuple(nextList)]=tempVal
                if tempVal<HValtemp:
                    tempList=nextList
                    HValtemp=tempVal

        for i in neighbor:
            print(i,neighbor[i])

        if(HVal>HValtemp):
            HVal=HValtemp
            current=tempList
            print("Current State : ", current, HVal)
        else:
            print("Final State : ", current, HVal)
            break

def addEdge(s,t,w):
    edges[s][t]=w
    edges[t][s]=w

if __name__=="__main__":
    addEdge(0,1,10)
    addEdge(0,2,20)
    addEdge(0,3,25)
    addEdge(0,4,15)
    addEdge(1,2,18)
    addEdge(1,3,17)
    addEdge(1,4,22)
    addEdge(2,3,13)
    addEdge(2,4,24)
    addEdge(3,4,16)
    hillClimb()
