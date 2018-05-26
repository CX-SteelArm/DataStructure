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
    for t in arc:
        weight = 1
        if len(arc[0]) == 2:
            tmpi, tmpj = t
        elif len(arc[0]) == 3:
            tmpi, tmpj, weight = t
        i, j = g.locateVex(tmpi), g.locateVex(tmpj)
        g.adjmx[i][j] = weight
        if g.kind == "unorder":
            g.adjmx[j][i] = g.adjmx[i][j]

    return g

# 构造一个无限大类
class Inf():
    def __init__(self):
        pass

    def __add__(self, a):
        return self

    def __radd__(self, a):
        return self.__add__(a)

    def __lt__(self, a):
        return False

    def __gt__(self, a):
        if isinstance(a, Inf):
            return False
        else:
            return True

    def __le__(self, a):
        return self.__lt__(a)

    def __ge__(self, a):
        return self.__gt__(a)

    def __repr__(self):
        return 'inf'


def floyd(g):
    dim = g.vexnum
    adjmx = g.adjmx
    path = [[0]*dim for i in range(dim)]
    
    for i in range(dim):
        for j in range(dim):
            path[i][j] = -1
            if adjmx[i][j] == 0 and i != j:
                adjmx[i][j] = Inf()

    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                if adjmx[i][j] > adjmx[i][k] + adjmx[k][j]:
                    adjmx[i][j] = adjmx[i][k] + adjmx[k][j]
                    if i == j and adjmx[i][j] < 0:
                        return False
                    path[i][j] = k

    return adjmx, path

def getInput():
    m, n = 0, 1
    arc = []
    while n != 0:
        s = [eval(i) for i in input().split()]
        if m == 0:
            m, n = s
        else:
            arc.append(s)
            n -= 1
    return m, arc

vexnum, arc = getInput()

g = createGraph(vexnum, len(arc), list(range(1, vexnum+1)), arc, "unorder")

D, path = floyd(g)

def printDAndPath():
    for i in D:
        print(i)

    for j in path:
        print(j)

def output():
    minTimes = []
    canChangeto = 0
    for i in D[0]:
        if i != 0 and not isinstance(i, Inf):
            canChangeto += 1

    if canChangeto != g.vexnum-1:
        print("0")
        return

    for i in D:
        m = max(i)
        minTimes.append(m)
    minTime = min(minTimes)
    index = minTimes.index(minTime)
    print(g.vexs[index], minTime)

output()