# 图的数组存储方式，对稠密关系很好

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

def dfsTraversal(g):
    visit = [0] * g.vexnum

    def dfs(g, i):
        visit[i] = 1
        print(g.vexs[i])
        adjlist = []
        for j in range(g.vexnum):
            if g.adjmx[i][j] == 1:
                adjlist.append(j)

        for j in adjlist:
            if visit[j] == 0:
                dfs(g, j)
    
    for i in range(g.vexnum):
        if visit[i] == 0:
            dfs(g, i)

def bfsTraversal(g):
    visit = [0] * g.vexnum
    queue = []
    queue.append(0)
    visit[0] = 1
    print(g.vexs[0])
    while len(queue) != 0:
        p = queue.pop(0)
        neighbor = []
        for j in range(g.vexnum):
            if g.adjmx[p][j] != 0:
                neighbor.append(j)
        for j in neighbor:
            if visit[j] == 0:
                visit[j] = 1
                print(g.vexs[j])
                queue.append(j)

vexs = ['A', 'B', 'C', 'D', 'E']
arc = [['A', 'C'], ['C', 'D'], ['D', 'E'], ['D', 'B']]
g = createGraph(5, 4, vexs, arc)
bfsTraversal(g)
