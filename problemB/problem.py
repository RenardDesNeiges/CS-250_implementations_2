#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import copy
stdin = sys.stdin


def thresh(nodes, edges):
    root = 1
    goal = nodes[-1]

    def succ(n):
        s = []
        for edge in edges:
            if edge[0][0] == n and not edge[0][1] in discovered and not edge[0][1] in s:
                s.append( ( edge[0][1], edge[1]) )
            if edge[0][1] == n and not edge[0][0] in discovered and not edge[0][0] in s:
                s.append( ( edge[0][0], edge[1]) )
        return s

    cost = 0
    Q = []
    discovered = [root]
    Q.append( (root, 0 ) )
    while len(Q)> 0:
        Q.sort(key = (lambda x : x[1]), reverse=False)
        # print("Q = " + str(Q))
        e = Q.pop()
        v = e[0]
        cost = e[1]
        # print("vertex = " + str(v))
        # print("cost = " + str(cost))
        if v == goal:
            return cost
        s = succ(v)
        for e in s:
            if e[1] > cost:
                cost = e[1]
            Q.append( (e[0],cost) )
            discovered.append(e[0])


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
    