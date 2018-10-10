# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:59:57 2018

@author: ASUS
"""

def myMax(myList):
    """求列表中的最大值
    
    myList：输入的列表
    return：列表中最大值"""
    if len(myList) == 1 :
        return myList[0]
    if len(myList) == 0 :
        return None
    else :
        return myList[0] if myList[0] > myMax(myList[1:]) else myMax(myList[1:])
print(myMax([1,3,56,13,54]))
print(myMax([3]))
print(myMax([]))