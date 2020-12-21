#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import array
import heapq as hq
from collections import defaultdict
stdin = sys.stdin


def thresh(aMat,goal):
    root = 1
    # goal = nodes[-1]


    # SUCCESSOR FUNCTION
    def succ(n,cost):
        s = []
        
        # def notDiscovered(step,cost):
        #     for el in discovered:
        #         if el[0] == step[0] and step[1] < cost:
        #             return False
        #     return True

        # print(discovered)
        # for edge in edges:
        #     step = (edge[0][1], max(edge[1],cost))
        #     if edge[0][0] == n and not step in s:
        #         s.append( step )
        #         edges.remove( edge )
        #     else:
        #         step = (edge[0][0], max(edge[1],cost))
        #         if edge[0][1] == n and not step in s:
        #             s.append( step )
        #             edges.remove( edge )

        for key in aMat[n]:
            if aMat[n][key] != -1:
                s.append( (key,max(aMat[n][key],cost)) )
                aMat[n][key] = -1
                aMat[key][n] = -1
        return s


    # Threshold-Dikjstra of smth idk
    Q = [ (root, 0 ) ]
    while len(Q)> 0:
        v, cost = Q.pop(0)
        # getting successors from the node
        s = succ(v,cost)
        # add successors to the queue
        s.sort(key = (lambda x : x[1]))
        for e in s:
            Q.append( e )

        # Q = list(merge(Q,s))
        # discovered = list(merge(discovered,s))

        # Queue sorting
        Q.sort(key = (lambda x : x[1]) )

        # print("Q = " + str(Q))        
        # print("vertex = " + str(v))
        # print("cost = " + str(cost))
        
        if v == goal:
            return cost

if not sys.stdin.isatty():

    il = 0
    edges = []
    aMat = defaultdict(dict)

    """
        loading buffer data
    """
    for line in sys.stdin:
        lst = line.split(' ')
        if il == 0:
            nn = int(lst[0])
            ne = int(lst[1])
        else:
            # edge = ( ( int(lst[0]) , int(lst[1]) ) , int(lst[2]) )
            aMat[ int(lst[0]) ][int(lst[1])] = int(lst[2])
            aMat[ int(lst[1]) ][int(lst[0])] = int(lst[2])
            # edges.append(edge)
        il += 1

    # nodes = list(range(1,nn+1))

    # print(edges)

    cost = thresh(aMat,nn)
    print(str(cost))
    