# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:20:24 2018

@author: Srammy
"""
from collections import deque
#利用字典（散列表）构建图,便与实现对应关系。要注意，字典（散列表）是无序的
graph={}
graph['you']=['bob','alice','claire']
graph['bob']=['anuj','peggy']
graph['alice']=['peggy']
graph['claire']=['jonny','thon']
graph['anuj']=[]
graph['peggy']=[]
graph['jonny']=[]
graph['thon']=[]

def breadth_first_search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[] #用于记录检查过的人。防止死循环
    while search_queue: #只要队列不为空
        person = search_queue.popleft()#取出一个人
        if person not in searched: #从队列取出的人没被检查过
            if person_is_seller(person): #如果这个人是卖家
                print(person+' is a seller')
                return True
            else:
                search_queue+=graph[person] #将邻居加入队列
                searched.append(person)     #已经检查过
    return False

def person_is_seller(name):
    '''判断是否是卖方'''
    return name[-1] == 'n' #名字是否以n结尾
breadth_first_search('you')
