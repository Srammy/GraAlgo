# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:29:02 2018

@author: ASUS
"""

def count(myList):
    """递归求列表中元素个数
    
    myList:一个列表
    return：元素个数"""
    if myList == [] :
        return 0
    else :
        return 1+count(myList[1:])
    
print(count([1,2,3,41,2]))
print(count([1]))
print(count(["1"]))
print(count([]))