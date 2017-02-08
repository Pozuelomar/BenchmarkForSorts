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

def bubbleSort(myList): # This is an aberration
    e=len(myList)
    while e!=0:
        last=0
        for i in range(e-1):
            if myList[i]>myList[i+1]:
                myList[i],myList[i+1]=myList[i+1],myList[i]
                last=i+1
        e=last
    return(myList)

def selectionSort(myList): # Basic myList, but not the fastest one
    for i in range(len(myList)-1):
        e=min(range(i,len(myList)),key=myList.__getitem__)
        myList[i],myList[e]=myList[e],myList[i]
    return(myList)

def insertionSort(myList): # This is the real one not the gnome myList
    for i in range(len(myList)):
        temp=myList[i]
        j=i-1
        while j>=0 and myList[j]>temp:
            myList[j+1]=myList[j]
            j-=1
        myList[j+1]=temp
    return(myList)

def shellSort(myList): # "An algorithm must be seen to be believed" Donald Knuth
    l=[0, 1, 4, 10, 23, 57, 132, 301, 701]
    pas=701
    while pas<len(myList):
        pas=round(pas*2.3)
    while pas:
        for d in range(pas):
            for i in range(len(myList))[d::pas]:
                temp=myList[i]
                j=i-pas
                while j>=0 and myList[j]>temp:
                    myList[j+pas]=myList[j]
                    j-=pas
                myList[j+pas]=temp
        try:
            pas=l[l.index(pas)-1]
        except Exception:
            pas = round(pas/2.3)
    return(myList)

def quickSort(myList): # Well, really slow if the job is allready done...
    def quickSortAux(myList,a,b):
        if a+1<b:
            i=a+1
            j=b-1
            while i<=j:
                while i<b and myList[i]<myList[a]:
                    i+=1
                while j>a and myList[j]>=myList[a]:
                    j-=1
                if i<j:
                    myList[i],myList[j]=myList[j],myList[i]
                    i+=1
                    j-=1
            myList[j],myList[a]=myList[a],myList[j]


            quickSortAux(myList,a,j)
            quickSortAux(myList,j+1,b)
    quickSortAux(myList,0,len(myList))
    return(myList)


def fusionSort(myList): # Well, really slow if the job is allready done...
    def fusionSortAux(myList,a,b):
        if a+1<b:
            m=(a+b)//2
            fusionSortAux(myList,a,m)
            fusionSortAux(myList,m,b)
            i=a
            j=m
            l=[]
            while i!=m or j!=b:
                if j==b:
                    l.append(myList[i])
                    i+=1
                elif i==m:
                    l.append(myList[j])
                    j+=1
                elif myList[i]<myList[j]:
                    l.append(myList[i])
                    i+=1
                else:
                    l.append(myList[j])
                    j+=1
            for i in range(b-a):
                myList[a+i]=l[i]

    fusionSortAux(myList,0,len(myList))
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
sortsToTest=[bubbleSort,selectionSort,insertionSort,shellSort,quickSort,fusionSort]

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
                error=True

            n=int(n*precision_rate)+1
        plt.plot(x,y)
        plt.text(x[-1], y[-1], s.__name__)
    plt.axis([0.0, maxLength*1.2, 0, maxTime*1.1])
    maxLength=0
    maxTime=0
    if i>=len(listsToSort)-w:
        plt.xlabel('length')
    plt.ylabel('time')
    plt.title(t.__name__)
plt.show()
