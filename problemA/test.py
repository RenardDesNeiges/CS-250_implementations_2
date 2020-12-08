#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import copy
from problem import maxFlow

# print("OPENING FILE")

# f = open("tests/01.txt", "r")
# lines = f.readlines()
# for line in lines:
#     print(line,end="")


def loadProblem(path):
    il = 0
    edges = []

    """
        loading buffer data
    """
    f = open(path, "r")
    lines = f.readlines()

    for line in lines:
        lst = line.split(' ')
        if il == 0:
            nn = int(lst[0])
            ne = int(lst[1])
        else:
            edges.append([int(lst[0]),int(lst[1])])
        il += 1

    nodes = list(range(1,nn+1))

    return nodes, edges

def loadSol(path):

    f = open(path, "r")
    lines = f.read()
    return int(lines.split(' ')[0])

ns = 0

print("Running tests : \n")

for i in range(1,9):
    infile = "tests/0" + str(i) + ".txt"
    solfile = "checks/0" + str(i) + ".txt"
    nodes, edges = loadProblem(infile)
    sol = loadSol(solfile)
    try:
        cNP = maxFlow(nodes,edges)
        if cNP == sol:
            print("    -> Success on test " + str(i))
            ns += 1
        else:
            print("    -> wrong answer on test " + str(i))
    except:
        print("    -> Program crashed on test " + str(i))

print("\nProgramm sucessufl on " + str(ns) +"/8 tests")