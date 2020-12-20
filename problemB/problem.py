#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import array
import heapq as hq
stdin = sys.stdin


def thresh(nodes, edges, discovered):
    root = 1
    goal = nodes[-1]

    # SUCCESSOR FUNCTION
    def succ(n,q,discovered):
        s = []
        # rmList = []
        for i in range(len(edges)):
            step = ( max(edges[i][0],cost), edges[i][1][1] )
            if edges[i][1][0] == n and not step in q and not discovered[i]:
                hq.heappush(q,step)
                # rmList.append( edges[i] )
                discovered[i] = True

            else:
                step = (max(edges[i][0],cost), edges[i][1][0])
                if edges[i][1][1] == n and not step in q and discovered[i]:
                    hq.heappush(q,step)
                    # rmList.append( edges[i] )
                    discovered[i] = True


        # for edge in rmList:
        #     edges.remove( edge )
        return s    


    # Threshold-Dikjstra of smth idk
    Q = [ ( 0, root ) ]

    hq.heapify(Q)

    Q.sort(key = (lambda x : x[0]) )
    while len(Q)> 0:
        cost, v = hq.heappop(Q)
        # getting successors from the node
        s = succ(v,Q,discovered)
        # add successors to the queue
        # s.sort(key = (lambda x : x[0]))
        # for e in s:
        #     if e not in Q:
        #         Q.append( e )
        # Q.sort(key = (lambda x : x[0]) )
        # print(Q)
        # print(s)
        Q = list(hq.merge(Q,s))

        hq.heapify(Q)

        # print(Q)

        if v == goal:
            return cost

if not sys.stdin.isatty():

    il = 0
    edges = []
    discovered= []

    """
        loading buffer data
    """
    for line in sys.stdin:
        lst = line.split(' ')
        if il == 0:
            nn = int(lst[0])
            ne = int(lst[1])
        else:
            edge = ( int(lst[2]) , ( int(lst[0]) , int(lst[1]) ) )
            edges.append(edge)
            discovered.append(False)
        il += 1

    nodes = list(range(1,nn+1))
    cost = thresh(nodes,edges,discovered)
    print(cost)
    