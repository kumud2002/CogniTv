def bubble_sort(L):
    n = len(L)

    for i in range(n):
        swapped  = False # Flag to keep check if the list is already sorted. 
        for j in range(0,n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                swapped = True
        if not swapped:
            break

df = [64,34,25,12,22,11,90]
print("Unsorted List :", df)
bubble_sort(df)
print("Sorted List :", df)