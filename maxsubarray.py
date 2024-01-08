def max_subarray_sum(arr):
    min_sum = 0
    pref_sum = 0
    ans = float('-inf')

    for num in arr:
        pref_sum += num
        ans = max(ans, pref_sum - min_sum)
        min_sum = min(min_sum, pref_sum)

    return max(ans, 0)  # Using max function to handle the case when ans is negative

# Example usage:
arr = [1, -2, 3, -1, 2]
result = max_subarray_sum(arr)
print(result)
