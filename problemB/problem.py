#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import array
import heapq as hq
from collections import defaultdict
stdin = sys.stdin


def thresh(aMat,goal):
    root = 1

    # Threshold-Dikjstra of smth idk, using a heap priority queue and adjacency matrices
    Q = [ (root, 0 ) ]
    while len(Q)> 0:

        v, cost = hq.heappop(Q)
        # getting successors from the node

        for key in aMat[v]:
            if aMat[v][key] != -1:
                hq.heappush( Q , (key,max(aMat[v][key],cost)) )
                aMat[v][key] = -1
                aMat[key][v] = -1
        
        # checking if we reached the goal node
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
            aMat[ int(lst[0]) ][int(lst[1])] = int(lst[2])
            aMat[ int(lst[1]) ][int(lst[0])] = int(lst[2])

        il += 1

    cost = thresh(aMat,nn)
    print(str(cost))
    