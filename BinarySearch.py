# ----------------Using Recursive Approach------------------
# TC : o(log n)
# SC : o(log n) [Call Stack by Recursion]

def binary_search_recurr(L,low,high,trgt):
    if high>=low:
        mid = (high + low) // 2
        if L[mid] == trgt:
            return mid
        elif L[mid]>trgt:
            return binary_search_recurr(L,low,mid-1,trgt)
        else:
            return binary_search_recurr(L,mid+1,high,trgt)
    else:
        return -1

#------------------Using Iterative Approach--------------------
# TC : o(log n)
# SC : o(1)
    
def binary_search_iterative(L,trgt):
    low = 0
    high = len(L) - 1
    mid = 0
    while low<=high:
        mid = (high + low) // 2
        if L[mid]<x:
            low = mid +1
        elif L[mid]>x:
            high = mid - 1
        else:
            return mid
    return -1

#------------------Using built-in bisect module--------------------
# TC : o(log n)
# SC : o(1)

import bisect

def binary_search_bisect(L,trgt):
    i = bisect.bisect_left(L,trgt)
    if i != len(L) and L[i] == trgt:
        return i
    else:
        return -1

df = [2,3,4,10,40]
x = 10

resultr = binary_search_recurr(df,0,len(df)-1,x)
if resultr !=-1:
    print("Element present at index :",str(resultr))
else:
    print("Element not present in data.")

resulti = binary_search_iterative(df,x)
if resulti !=-1:
    print("Element present at index :",str(resulti))
else:
    print("Element not present in data.")

resultb = binary_search_bisect(df,x)
if resultb !=-1:
    print("Element present at index :",str(resultb))
else:
    print("Element not present in data.")
