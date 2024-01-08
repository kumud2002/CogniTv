import math

def minimize_maximum(d1,d2,uc1,uc2):

    l, r = 1, 10**18
    ans = -1
    lcm = math.lcm(d1,d2)
    
    while l <= r:
        m = (l+r)//2 #mid

        c1 = m - (m//d1)
        c2 = m - (m//d2)
        common = m-m//lcm

        tc = c1+c2+common

        if c1 >= uc1 and c2 >= uc2 and common>=uc1+uc2:
            ans = m
            r=m-1 
        else:
            l=m+1
    return int(ans)

print(minimize_maximum(2,4,8,2))