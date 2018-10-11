# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:52:23 2018

@author: Srammy
"""

def binary_search(arr,low,high,item):
    """递归实现二分查找
    
    arr:列表
    low:第一个元素的索引
    high:最后一个元素的索引
    item:要找到的项
    return:item在arr里的索引"""
    if low > high :
        return -1
    else:
        mid = (low + high) // 2
        if item == arr[mid]:
            return mid
        else:
            if item < arr[mid] :
                return binary_search(arr,low,mid-1,item)  #low high 将arr分段
            else:
                return binary_search(arr,low+1,high,item)

myList=[1,3,5,7,9,22,45,94]
print(binary_search(myList,0,len(myList)-1,22))
print(binary_search(myList,0,len(myList)-1,2))
print(binary_search(myList,0,len(myList)-1,3))
print("###############################")
myList1=[1,2]
print(binary_search(myList1,0,len(myList1)-1,22))
print(binary_search(myList1,0,len(myList1)-1,1))
print("###############################")
myList2=[1]
print(binary_search(myList2,0,len(myList2)-1,22))
print(binary_search(myList2,0,len(myList2)-1,1))