def maxSubarraySum(arr, n) :
    curSum = [0 for i in range(n)] 
    maxSum = 0
    for i in range(n) :
        if(i == 0) :
            curSum[i] = max(curSum[i], arr[i])
        else :
            curSum[i] = max(curSum[i], curSum[i-1] + arr[i])   

        maxSum = max(maxSum, curSum[i]) 
    return maxSum
