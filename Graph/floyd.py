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

vexs = ['v' + str(i) for i in range(6)]
arc = [['v0', 'v5', 100], ['v0', 'v2', 10], ['v0', 'v4', 30], ['v2', 'v3', 50], ['v1', 'v2', 5], ['v3', 'v5', 10], ['v4', 'v3', 20], ['v4', 'v5', 60]]
g = createGraph(6, 8, vexs, arc, "order")

D, path = floyd(g)

for i in D:
    print(i)

for j in path:
    print(j)
