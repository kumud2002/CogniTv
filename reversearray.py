from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    # Write your code here.
    a=arr[:m+1]
    b=arr[m+1:] 
    c=b[::-1]
    d=a+c
    return d
            