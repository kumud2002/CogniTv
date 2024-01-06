def quick_sort(L):
    if len(L) <= 1:
        return L
    
    pivot = L[len(L)//2]
    left = [i for i in L if i < pivot]
    middle = [j for j in L if j == pivot]
    right = [k for k in L if k > pivot]

    return quick_sort(left) + middle + quick_sort(right)

df = [3,6,8,10,1,2,2,1]
print("Unsorted List :",df)
df = quick_sort(df)
print("Sorted List :",df)