def kth_smallest_largest(L,k):
    n = len(L)
    L.sort()
    return L[k-1], L[n-k]

df = [23,78,33,1,19,44,89,37,17]
result = list(kth_smallest_largest(df,3))
print("Largest is :",str(result[1]),"and Smallest is :",str(result[0]))