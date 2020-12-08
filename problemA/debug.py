#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import copy
from problem import maxFlow

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
        edges.append([int(lst[0]),int(lst[1])])
    il += 1

nodes = list(range(1,nn+1))

flow = maxFlow(nodes,edges)

print(flow)