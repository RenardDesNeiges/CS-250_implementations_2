#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import copy
stdin = sys.stdin

def maxFlow(nodes,edges):
     
     # ==> https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
    def BFS(root,goal):
        # ==> find the successor nodes to a given node
        def succ(n):
            s = []
            for edge in edges:
                if edge[0] == n and not edge[1] in discovered and not edge[1] in s:
                    s.append(edge[1])
                if edge[1] == n and not edge[0] in discovered and not edge[0] in s:
                    s.append(edge[0])
            return s

        path = []
        Q = []
        discovered = [root]
        Q.append( (root, [] ) )
        while len(Q)> 0:
            v, path = Q.pop()
            if v == goal:
                return path + [v]
            s = succ(v)
            for e in s:
                Q.append( (e,path + [v]) )
                discovered.append(e)

    go = True
    start = 1
    finish = len(nodes)

    pathNb = 0

    while go:
        path = BFS(start,finish)
        if path is None:
            go = False
        else:
            for i in range(1, len(path)):
                edge = [path[i-1],path[i]]
                if edge in edges:
                    edges.remove(edge)
                else:
                    redge = [path[i],path[i-1]]
                    edges.remove(redge)

            pathNb += 1
    return pathNb

    #############################################################
    #########                                           #########
    #########        UNCOMMENT WHEN HANDING OUT         #########
    #########                                           #########
    #############################################################



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
            edges.append([int(lst[0]),int(lst[1])])
        il += 1

    nodes = list(range(1,nn+1))

    flow = maxFlow(nodes,edges)

    print(flow)