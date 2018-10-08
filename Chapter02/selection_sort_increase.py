# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:21:44 2018

@author: Srammy

intro：选择排序算法（递增） 时间复杂度O(n^2)
"""
def findSmallest(arr):
    """find the smallest value in the arr
       arr:进行操作的序列
       return：最小值的索引值
    """
    min = arr[0]
    min_index = 0
    for i in range(1,len(arr)):
        if arr[i] < min :
            min=arr[i]
            min_index=i
    return min_index

def select_sort_increse(arr):
    """
    选择排序
    arr:进行操作的序列
    return ：排好序的序列
    """
    #要循环len(arr)次,每次都要找出最小值并弹出
    result = []
    for i in range(len(arr)):
        min_index = findSmallest(arr)
        result.append(arr.pop(min_index))
    
    return result

print(select_sort_increse([12,8,55,55,100,3,30]))
        
        