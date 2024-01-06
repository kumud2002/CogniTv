def selection_sort(L):
    n = len(L)

    for i in range(n-1):
        minidx = i
        for j in range(i+1,n):
            if L[j] < L[minidx]:
                minidx = j
        L[i], L[minidx] = L[minidx], L[i]

df = [64,25,12,22,11]
print("Unsorted List :",df)
selection_sort(df)
print("Sorted List :",df)