#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import copy
from problem import thresh


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
            edge = ( int(lst[1]) ) , int(lst[2]) , ( int(lst[0]) )
            edges.append(edge)
        il += 1

    nodes = list(range(1,nn+1))
    return nodes, edges

def loadSol(path):

    f = open(path, "r")
    lines = f.read()
    return int(lines.split(' ')[0])

ns = 0

print("Running tests : \n")

for i in range(1,7):
    infile = "tests/0" + str(i) + ".txt"
    solfile = "checks/0" + str(i) + ".txt"
    nodes, edges = loadProblem(infile)
    sol = loadSol(solfile)
    try:
        cost = thresh(nodes,edges)
        if cost == sol:
            print("    -> Success on test " + str(i))
            ns += 1
        else:
            print("    -> wrong answer on test " + str(i))
    except:
        print("    -> Program crashed on test " + str(i))

print("\nProgram successful on " + str(ns) +"/6 tests")