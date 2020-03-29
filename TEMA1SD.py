import time
from random import *

def TestSort(sortedArray, initArray):
    if len(sortedArray)!=len(initArray):
        return False
    else:
        initArray.sort()
        for i in range(len(initArray)):
            if initArray[i]!=sortedArray[i]:
                return False
    return True


def BubbleSort(array):
    if len(array)>5000:
        return "Prea multe numere => un timp foarte mare de executie"
    ok=True
    n=len(array)
    j=0
    while(ok==True and n>1):
        ok=False
        for i in range(len(array)-j-1):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
                ok=True
        n-=1
        j+=1
    return array

def CountSort(array):
    if len(array)==0:
        return []
    valMax=max(array)
    if valMax>750000:
        return "Numere prea mari pentru a efectua countsort"
    countarray=[0]*(valMax+1)
    for i in array:
        countarray[i]+=1
    k=0
    for i in range(valMax+1):
        for j in range(countarray[i]):
            array[k]=i
            k+=1
    return array



def Interclasare(arrayst, arraydr):
    i=j=0
    list=[]
    while i<len(arrayst) and j<len(arraydr):
        if arrayst[i]<arraydr[j]:
            list.append(arrayst[i])
            i+=1
        else:
            list.append(arraydr[j])
            j+=1
    list.extend(arrayst[i:])
    list.extend(arraydr[j:])
    return list

def MergeSort(array):
    if len(array)<=1:
        return array
    else:
        arrayst=MergeSort(array[:len(array)//2])
        arraydr=MergeSort(array[len(array)//2:])
        return Interclasare(arrayst, arraydr)



def CountSortRadix(array,base,pos):
    countArray=[0]*base
    outputArray=[0]*len(array)
    for i in range(len(array)):
        countArray[array[i]//(base**pos)%base]+=1
    for i in range (1,base):
        countArray[i]=countArray[i]+countArray[i-1]
    for i in range(len(array)-1,-1,-1):
        outputArray[countArray[(array[i]//base**pos)%base]-1]=array[i]
        countArray[((array[i]//base**pos)%base)%base]-=1
    return outputArray

def RadixSort(array,base):
    if len(array)==0:
        return []
    valMax=max(array)
    poss=0
    while(valMax):
        valMax=valMax//base
        poss+=1
    for pos in range(poss):
        array=CountSortRadix(array,base,pos)
    return array

def median_of_medians(array):
    if len(array)<=5:
        return sorted(array)[len(array)//2]
    sublists=[sorted(array[i:i + 5]) for i in range(0, len(array), 5)]
    med=[s[len(s) // 2] for s in sublists]
    return median_of_medians(med)

def QuickSort(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    pivot = median_of_medians(array)
    arrayst = []
    arraydr = []
    arrayeq = []
    for i in array:
        if i < pivot:
            arrayst.append(i)
        elif i == pivot:
            arrayeq.append(i)
        else:
            arraydr.append(i)
    arrayst = QuickSort(arrayst)
    arraydr = QuickSort(arraydr)
    arrayst.extend(arrayeq)
    arrayst.extend(arraydr)
    return arrayst

sortari=[sorted, BubbleSort, CountSort, MergeSort, RadixSort, QuickSort]

Test=4
while Test:
    print("Testul ", Test, ": \n")
    maxVal=0
    numbers=0
    if Test==4:
        maxVal=100000
        numbers=1
    if Test==3:
        maxVal=0
        numbers=0
    if Test == 2:
        maxVal = 100000000
        numbers = 100000
    if Test==1:
        maxVal = 10
        numbers = 10

    RandomArray=[randint(0,maxVal) for i in range(numbers)]
    Test-=1
    print("Valoarea maxima este " + str(maxVal))
    print("Lungimea RandomArray este " + str(numbers))
    print()

    for Sort in sortari:
        print("Sortarea " + Sort.__name__ )
        StartingTime=time.time()
        if Sort==RadixSort:
            x=input('Baza in care vom efectua Radix este ')
            SortedArray=Sort(RandomArray,int(x))
        else:
            SortedArray=Sort(RandomArray)
        FinishTime=time.time()
        if isinstance(SortedArray,str):
            print(SortedArray)
            print('\n')
        elif TestSort(SortedArray,RandomArray):
            print("Sortare efectuata cu succes in " + str(FinishTime-StartingTime) + " secunde ")
            print('\n')
        else:
            print("Fail")


