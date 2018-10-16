# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:02:50 2018

@author: Srammy
"""
#使用了三个字典（散列表）

# the graph 图结构
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# the costs table  开销（从起点算）
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# the parents table 父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#已经被处理过的节点
processed = []
def Dijkstra (costs):
    #在未处理的节点中找到开销最小的点
    node = find_lowest_cost_node(costs)
    while node is not None :
        #记录下开销最小点的开销
        cost=costs[node]
        #找到开销最小点的领居
        neighbors=graph[node]
        for n in neighbors.keys(): #遍历当前节点的邻居
            #领居的开销（从起点算起）
            new_cost=cost+neighbors[n]
            #如果当前节点前往邻居更近
            if costs[n] > new_cost:
                costs[n]=new_cost #更新该邻居的开销
                parents[n]=node    #将该令居的父节点设为当前节点
        processed.append(node) #标记为已处理
        node = find_lowest_cost_node(costs) #找到接下来要处理的点
        
def find_lowest_cost_node(costs):
    """在未处理的节点中找到开销最小的点"""
    lowest_cost=float("inf")
    lowest_cost_node=None
    #遍历所有的节点
    for node in  costs:
        cost = costs[node]
        #如果节点的开销更低且没被处理过
        if cost < lowest_cost and node not in processed :
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node

Dijkstra(costs)
print(costs)
print(parents)