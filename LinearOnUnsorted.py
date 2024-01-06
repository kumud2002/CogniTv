def linear_search(L,e):
    found = False
    for i in L:
        if i==e:
            found=True
            break
    return found

arr = [1,2,3,4,5,6,7,8,9,10,45,33]
trgt = 45

result = linear_search(arr,trgt)
if result:
    print("Element Found")
else:
    print("Element Not Found")