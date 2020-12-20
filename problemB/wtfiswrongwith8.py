#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import array
import networkx as nx
import matplotlib.pyplot as plt
stdin = sys.stdin

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

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from( [ (e[0][0],e[0][1], e[1]) for e in edges] )

    print(G)
    pos = nx.kamada_kawai_layout(G)
    labels = nx.get_edge_attributes(G,'weight')
    edg,weights = zip(*nx.get_edge_attributes(G,'weight').items())
    nx.draw(G,pos,with_labels = True,node_color='#fc4528',width=4.0,edge_color=weights,edge_cmap=plt.cm.hot)
    nx.draw_networkx_edge_labels(G,pos,labels)
    plt.show()

    