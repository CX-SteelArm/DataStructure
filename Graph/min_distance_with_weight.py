class Gragh_list():
    def __init__(self, v, a, vexs, arc, k="unorder"):
        self.kind = k
        self.vexnum = v
        self.arcnum = a
        self.vexs = vexs
        self.arc = arc
        self.adjmx = []

    def locateVex(self, k):
        for i in range(self.vexnum):
            if self.vexs[i] == k:
                return i
        else:
            return -1

def createGraph(v, a, vexs, arc, kind="unorder"):
    g = Gragh_list(v, a, vexs, arc, kind)
    # 初始化
    # g.adjmx = [[0] * v] * v 这样生成每行关联，错误
    g.adjmx = [[0]*v for i in range(v)]
    # 连接顶点
    dim = len(arc[0])
    for t in arc:
        weight = 1
        if dim == 2:
            tmpi, tmpj = t
        elif dim == 3:
            tmpi, tmpj, weight = t
        i, j = g.locateVex(tmpi), g.locateVex(tmpj)
        g.adjmx[i][j] = weight
        if g.kind == "unorder":
            g.adjmx[j][i] = g.adjmx[i][j]

    return g

# Dijkstra算法
def minDistance(g, e):
    i = g.locateVex(e)
    INF = 65535
    dlist = [INF] * g.vexnum
    dlist[i] = 0
    collect = []

    while True:
        i = findMinDist(g, dlist, collect)
        if i < 0:
            break
        n = findNeighbor(g, i)
        for j in n:
            dlist[j] = min(dlist[i] + g.adjmx[i][j], dlist[j])
        collect.append(i)

    return dlist
        
def findNeighbor(g, i):
    neighbor = []
    for j in range(g.vexnum):
        if g.adjmx[i][j] != 0:
           neighbor.append(j) 
    return neighbor

def findMinDist(g, dlist, collect):
    minDis = 65535
    j = -1
    for i in range(len(dlist)):
        if i not in collect and dlist[i] < minDis:
            minDis = dlist[i]
            j = i
    return j

vexs = ['v' + str(i) for i in range(6)]
arc = [['v0', 'v5', 100], ['v0', 'v2', 10], ['v0', 'v4', 30], ['v2', 'v3', 50], ['v1', 'v2', 5], ['v3', 'v5', 10], ['v4', 'v3', 20], ['v4', 'v5', 60]]
g = createGraph(6, 8, vexs, arc, "order")
print(minDistance(g, 'v0'))

