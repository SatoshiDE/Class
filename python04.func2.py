#!/usr/bin/env python

def fact1(n):
    """ 'n!' を求める """
    ans = 1
    i = 1
    for i in range(1, n+1):
        ans = ans * i
        i = i + 1
    return(ans)

c = fact1(4)
print(c)
