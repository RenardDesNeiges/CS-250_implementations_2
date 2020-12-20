#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import copy
from problem import thresh
import cProfile
import pstats
import io
from pstats import SortKey

# print("OPENING FILE")

# f = open("tests/01.txt", "r")
# lines = f.readlines()
# for line in lines:
#     print(line,end="")


def loadProblem(path):

    f = open(path, "r")
    lines = f.readlines()

    il = 0
    edges = []

    """
        loading buffer data
    """
    for line in lines:
        lst = line.split(' ')
        if il == 0:
            nn = int(lst[0])
            ne = int(lst[1])
        else:
            edge = ( ( int(lst[0]) , int(lst[1]) ) , int(lst[2]) )
            edges.append(edge)
        il += 1

    nodes = list(range(1,nn+1))
    return nodes, edges
infile = "tests/16.txt"

nodes, edges = loadProblem(infile)
cost = cProfile.run("thresh(nodes,edges)")

pr = cProfile.Profile()
pr.enable()
cost = thresh(nodes,edges)
pr.disable()
print("cost = "  + str(cost) +"\n")
# cost = thresh(nodes,edges)
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
