# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:20:28 2018

@author: Srammy

递归：函数调用自身
递归其实就是循环
"""

def countdown(n):
    """倒计时
    
    n：起始值
    return：None"""
    if n == 0 : #基线条件
        return None
    else:       #递归条件
        print(n)
        countdown(n-1)
        
countdown(10)