# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:40:53 2018

@author: ASUS

选择排序-递减  时间复杂度O(n^2)
"""

def findmax(arr):
    """
    寻找序列中的最大值
    arr:操作的序列
    return ：最大值的索引
    """
    max_value = arr[0]
    max_index = 0
    for i in range(1,len(arr)):
        if arr[i] > max_value :
            max_value = arr[i]
            max_index = i
    return max_index

def selection_sort_decrease(arr):
    """
    选择排序
    """
    result=[]
    
    for i in range(len(arr)):
        max_index = findmax(arr)
        result.append(arr.pop(max_index))
        
    return result

print(selection_sort_decrease([12,8,55,55,100,3,30]))