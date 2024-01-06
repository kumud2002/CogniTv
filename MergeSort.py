def merge_sort(L):
    if len(L) > 1:
        mid = len(L)//2
        left, right = L[:mid], L[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i<len(left) and j<len(right):
            L[k], i, j, k = (left[i], i+1, j, k+1) if left[i]<right[j] else (right[j], i, j+1, k+1)
        while i<len(left): 
                L[k], i, k = left[i], i+1, k+1
        while j<len(right) : 
                L[k], j, k = right[j], j+1, k+1

df = [12,11,13,5,6,7]
print(df)
merge_sort(df)
print(df)
