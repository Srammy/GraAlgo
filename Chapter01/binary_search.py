# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:17:47 2018

@author: Srammy
"""

def binary_search(sequence,item):
    '''二分查找法
       时间复杂度O(logn)
       
       sequence:进行操作的有序序列
       item：要查找的对象
       return：找到时，返回item对应的索引值；找不到，返回None
    '''
    #low和high用于跟踪要在其中查找的列表部分
    low=0
    high=len(sequence)-1
    
    #要查找的列表部分缩小到只有一个元素为止
    while low <= high :
        mid = (low + high) // 2 #地板除，只取整数部分
        guess = sequence[mid]
        
        #找到了item，则返回索引值
        if item == guess :
            return mid
        
        #猜得的数过大
        if guess > item :
            high=mid-1
        #猜得的数过小
        else:
            low=mid+1
            
    #找不到item 
    return None

##########test################
myList=[1,3,5,7,9,11]
#存在
print(binary_search(myList,9))
#不存在
print(binary_search(myList,10))