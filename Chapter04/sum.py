# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:39:04 2018

@author: Srammy
"""
def mysum(arr):
    """分而治之策略写求和函数
    
    arr：列表，元素是整数
    return：列表元素之和"""
    if len(arr) == 1 :#基线条件
        return arr[0]
    else :            #递归条件
        print(arr)
        return arr[0]+mysum(arr[1:]) #这种传参方式是可行的
    
print(mysum([5,4,3,2,1]))