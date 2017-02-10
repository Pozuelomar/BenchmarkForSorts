"""
Written by Martin Pozuelo
For EISTI's class
"""

from random import*
from time import*
import matplotlib.pyplot as plt

"""
Parameters of the benchmark
Modifie the next values as you wish
"""

# Max time for a test
timeLimit=0.05

# Increase rate of number of element
precision_rate=1.1

# Number of each test to average
number_of_test=3

"""
Code your sorts here
"""

def bogoSort(myList): # Please, don't
    while not all(myList[i]<=myList[i+1]for i in range(len(myList)-1)):
        for i in range(len(myList)-1):
            e=randrange(i,len(myList))
            myList[i],myList[e]=myList[e],myList[i]
    return(myList)



"""
Generating to-sort lists
You can let this part of code
"""

def iShuffled(n):
    t=list(range(n))
    shuffle(t)
    return(t)

def iNearSorted(n):
    t=list(range(n))
    shuffle(t)
    t=[sorted(t[i::10]) for i in range(10)]
    t=[t[i%10][i//10] for i in range(n)]
    return(t)

def iSorted(n):
    t=list(range(n))
    return(t)

def iShuffledOccurences(n):
    return(list(int(random()*n/10) for _ in range(n)))

def iReversed(n):
    t=list(range(n))
    return(t[::-1])

def fShuffled(n):
    return(list(random() for _ in range(n)))

def fReversed(n):
    v=10
    t=list(random() for _ in range(n))
    t=[sorted(t[i::v]) for i in range(v)]
    t=[t[i%v][i//v] for i in range(n)]
    return(t)

"""
Verification fonction
"""

def isSorted(l):
    return(all(l[i]<=l[i+1]for i in range(len(l)-1)))


"""
Insert sorts and lists generator here
"""
# Insert here your sort to benchmark
sortsToTest=[bogoSort]

# Insert here your generators of lists to sort
listsToSort=[iShuffled,iNearSorted,iSorted,iShuffledOccurences,iReversed,fShuffled,fReversed]

"""
Benchmark, do not break everything plz, I won't repair it.
"""
h=0
w=0
while len(listsToSort)>h*w:
    h+=1
    if len(listsToSort)>h*w:
        w+=1


maxLength=0
maxTime=0
for i,t in enumerate(listsToSort):
    plt.subplot(h*100+w*10+1+i)
    for s in sortsToTest:
        n=0
        x=[]
        y=[]
        error=False
        while not error and (n==0 or y[-1]<timeLimit):

            try:
                ysum=0
                allSorted=True
                for _ in range(number_of_test):
                    l=t(n)
                    #print(l)
                    ti=time()
                    listSorted=s(list(l))
                    ysum+=time()-ti
                    allSorted = allSorted and isSorted(listSorted)
                # data_corrupted : wrong data in the output, not corresponding to values in input()
                print(("not_sorted","sorted")[allSorted],("data_corrupted","data_ok")[listSorted==sorted(l)],t.__name__,s.__name__,n,ysum/number_of_test)
                x+=[n]
                y+=[ysum/number_of_test]
                maxLength=max(maxLength,n)
                maxTime=max(maxTime,y[-1])
            except:
                print(t.__name__,s.__name__,n,"Error")
                traceback.print_exc()
                error=True

            n=int(n*precision_rate)+1
        plt.text(x[-1], y[-1], s.__name__,color=plt.plot(x,y)[0].get_color())
    plt.axis([0.0, maxLength*1.2, 0, maxTime*1.1])
    maxLength=0
    maxTime=0
    if i>=len(listsToSort)-w:
        plt.xlabel('length')
    plt.ylabel('time')
    plt.title(t.__name__)
plt.show()
