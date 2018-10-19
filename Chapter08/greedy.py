# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:49:07 2018

@author: ASUS

这是一个集合覆盖问题
"""
#要覆盖的州
states_needed=set(['mt','wa','or','id','nv','ut','ca','az'])

#可选择的广播台清单  使用散列表来实现
stations={}
stations['kone']=set(['id','nv','ut'])
stations['ktwo']=set(['wa','id','mt'])
stations['kthree']=set(['or','nv','ca'])
stations['kfour']=set(['nv','ut'])
stations['kfive']=set(['ca','az'])

#保存最后的结果，其中的站可以覆盖所有州
final_stations=[]

while states_needed : #只要还有未覆盖的州
    best_station = None  #所覆盖州最多的站
    states_covered=set() #被覆盖的州
    #每轮for循环都要找出覆盖余下未覆盖过得州中最多州的站
    for station,states in stations.items():#
        covered=states_needed & states  #取交集,covered包含当前广播台覆盖的一系列还未覆盖的州
        if len(covered) > len(states_covered) :
            best_stations = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.append(best_stations)

print(final_stations)