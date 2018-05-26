class Gragh_list():
    def __init__(self, v, a, vexs, arc, k="unorder"):
        self.kind = k
        self.vexnum = v
        self.arcnum = a
        self.vexs = vexs
        self.arc = arc
        self.adjmx = []
        self.pay = []

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
    g.pay = [[0]*v for i in range(v)]
    # 连接顶点
    for t in arc:
        tmpi, tmpj, weight, pay = t
        i, j = g.locateVex(tmpi), g.locateVex(tmpj)
        g.adjmx[i][j] = weight
        g.pay[i][j] = pay
        if g.kind == "unorder":
            g.adjmx[j][i] = g.adjmx[i][j]
            g.pay[j][i] = g.pay[i][j]

    return g

# Dijkstra算法
def minDistance(g, e):
    i = g.locateVex(e)
    INF = 65535
    dlist = [INF] * g.vexnum
    dlist[i] = 0
    collect = []
    # 到每个顶点的路径
    root = [[0]] * g.vexnum
    paylist = [0] * g.vexnum

    while True:
        i = findMinDist(g, dlist, collect)
        if i < 0:
            break
        n = findNeighbor(g, i)
        for j in n:
            if dlist[i] + g.adjmx[i][j] < dlist[j] or (dlist[i] + g.adjmx[i][j] == dlist[j] and paylist[i] + g.pay[i][j] < paylist[j]):
                dlist[j] = dlist[i] + g.adjmx[i][j]
                paylist[j] = paylist[i] + g.pay[i][j]
                tmp = root[i].copy()
                tmp.append(j)
                root[j] = tmp

        collect.append(i)

    return dlist, root, paylist
        
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

def getInput():
    m, n, start, end = 0, 1, 0, 0
    arc = []
    while n != 0:
        s = [eval(i) for i in input().split()]
        if m == 0:
            m, n, start, end = s
        else:
            arc.append(s)
            n -= 1
    return m, start, end, arc

m, start, end, arc = getInput()

g = createGraph(m, len(arc), list(range(m)), arc)

mindis, root, minpay = minDistance(g, start)
print(mindis[end], minpay[end])
# vexs = ['v' + str(i) for i in range(4)]
# arc = [['v0', 'v1', 1, 20], ['v0', 'v2', 2, 10], ['v1', 'v3', 3, 10], ['v2', 'v3', 2, 90]]
# g = createGraph(4, 4, vexs, arc, "order")
# print(minDistance(g, 'v0'))

