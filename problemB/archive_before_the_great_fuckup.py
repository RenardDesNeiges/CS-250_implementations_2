#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import copy
from heapq import merge 
stdin = sys.stdin


def thresh(nodes, edges):
    root = 1
    goal = nodes[-1]


    # SUCCESSOR FUNCTION
    def succ(n,cost):
        s = []
        
        def notDiscovered(step):
            for el in discovered:
                if el[0] == step[0]:
                    return False
            return True

        # print(discovered)
        for edge in edges:
            step = (edge[0][1], max(edge[1],cost))
            if edge[0][0] == n and notDiscovered(step) and not ( edge[0][1], edge[1]) in s:
                s.append( ( edge[0][1], max(edge[1],cost) ) )

            step = (edge[0][0], max(edge[1],cost))
            if edge[0][1] == n and not step in discovered and not ( edge[0][0], edge[1]) in s:
                s.append( ( edge[0][0], max(edge[1],cost) ) )
        return s


    # Threshold-Dikjstra of smth idk
    Q = []
    discovered = [(root, 0 )]
    Q.append( (root, 0 ) )
    while len(Q)> 0:
        v, cost = Q.pop(0)
        # getting successors from the node
        # (this is where this shitty implementation is the shittiest)
        s = succ(v,cost)
        # add successors to the queue
        s.sort(key = (lambda x : x[1]))
        for e in s:
            Q.append( e )
            discovered.append( e )

        # Q = list(merge(Q, s, key=(lambda x : x[1]) ))
        # discovered = list(merge(discovered, s, key=(lambda x : x[1]) ))


        Q.sort(key = (lambda x : x[1]) )

        # print("Q = " + str(Q))        
        # print("vertex = " + str(v))
        # print("cost = " + str(cost))
        
        if v == goal:
            return cost

if not sys.stdin.isatty():

    il = 0
    edges = []

    """
        loading buffer data
    """
    for line in sys.stdin:
        lst = line.split(' ')
        if il == 0:
            nn = int(lst[0])
            ne = int(lst[1])
        else:
            edge = ( ( int(lst[0]) , int(lst[1]) ) , int(lst[2]) )
            edges.append(edge)
        il += 1

    nodes = list(range(1,nn+1))

    cost = thresh(nodes,edges)
    print(str(cost))
    