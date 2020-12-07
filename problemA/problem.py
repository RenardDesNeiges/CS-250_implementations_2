#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
stdin = sys.stdin

# def maxFlow(nodes,edges):

     
     # ==> https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search

    # def BFS(root,goal,path):
    #     def succ(n):
    #         s = []
    #         for edge in edges:
    #             if edge[0] == n and not edge[1] in discovered and not edge[1] in s:
    #                 s.append(edge[1])
    #             if edge[1] == n and not edge[0] in discovered and not edge[0] in s:
    #                 s.append(edge[1])
    #         return s

    #     Q = []
    #     discovered = [root]
    #     Q.append( (root,[root]) )
    #     while len(Q)> 0:
    #         v,path = Q.pop()
    #         if v == goal:
    #             return path
    #         Q.append( (succ(v),path.append(node)) )

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


print("Node number : " + str(nn))
print("Edge number : " + str(ne))
print("Edges : " + str(edges))
print("Nodes : " + str(nodes))