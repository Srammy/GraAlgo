# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:29:25 2018

@author: ASUS
"""

def factorial(n):
    """计算n！
    
    n：正整数
    return：n！"""
    if n == 0 :#基线条件
        return 1
    else:      #递归条件
        return n*factorial(n-1)
    
print(factorial(3))
print(factorial(0))
print(factorial(1))