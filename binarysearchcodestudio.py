def search(nums: [int], target: int):
    # write your code logic !!
    l=len(nums)
    s=0
    e=l-1
    #if(s>e):
     #   return -1
    while(s<=e):
        mid=s+(e-s)//2
   # for i in range(0,l):
        if(nums[mid]==target):
            return mid
        elif(target<nums[mid]):
            e=mid-1
        else:
            s=mid+1
    return -1    




    
n= int (input())
arr = list(map(int,input().strip().split()))[:n]
target =int (input())
print (search(arr, target))