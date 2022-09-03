# Write your code here
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
class graph:
    def __init__(self, nv):
        self.nv = nv
        self.admat = [[0 for i in range(nv)] for j in range(nv)]

    def addedge(self, v1, v2):
        self.admat[v1][v2] = 1
        self.admat[v2][v1] = 1

    def removeedge(self, v1, v2):
        if self.containedge(v1, v2) is True:
            self.admat[v1][v2] = 0
            self.admat[v2][v1] = 0

    def containedge(self, v1, v2):
        if self.admat[v1][v2] == 1:
            return True
        else:
            return False

    def helperisConnected(self, visited, si):
        visited[si] = True
        for i in range(self.nv):
            if visited[i] == False and self.admat[si][i] == 1:
                self.helperisConnected(visited, i)
        return
        pass

    def isconnected(self):
        if self.nv == 0:
            return True
        visited = [False for i in range(self.nv)]
        self.helperisConnected(visited, 0)
        # print(visited)
        if all(visited) is True:
            return True
        else:
            return False


a = list(map(int, input().split(" ")))
v, e = a[0], a[1]
g = graph(v)
for i in range(e):
    b = list(map(int, stdin.readline().strip().split(" ")))
    g.addedge(b[0], b[1])

if g.isconnected():
    print("true")
else:
    print("false")