def linear_search(L,e):
    for i in L:
        if i==e:
            return True
        if i>e:
            return False


arr = [1,2,3,4,5,6,7,8,9,10,45,333]
trgt = 45

result = linear_search(arr,trgt)
if result:
    print("Element Found")
else:
    print("Element Not Found")