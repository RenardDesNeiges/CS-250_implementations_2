#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import array
stdin = sys.stdin


def thresh(nodes, edges):
    root = 1
    goal = nodes[-1]

    # SUCCESSOR FUNCTION
    def succ(n,cost):
        s = []
        rmList = []
        for edge in edges:
            step = (edge[0][1], max(edge[1],cost))
            if edge[0][0] == n and not step in s:
                s.append( step )
                rmList.append( edge )
            else:
                step = (edge[0][0], max(edge[1],cost))
                if edge[0][1] == n and not step in s:
                    s.append( step )
                    rmList.append( edge )

        for edge in rmList:
            edges.remove( edge )
        return s


    # Threshold-Dikjstra of smth idk
    Q = [ (root, 0 ) ]

    Q.sort(key = (lambda x : x[1]) )
    while len(Q)> 0:
        v, cost = Q.pop(0)
        # getting successors from the node
        s = succ(v,cost)
        # add successors to the queue
        s.sort(key = (lambda x : x[1]))
        for e in s:
            if e not in Q:
                Q.append( e )
        Q.sort(key = (lambda x : x[1]) )

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
    print(cost)
    