class Arc():
    def __init__(self, adj, info=None):
        self.adj = adj
        self.next = None
        self.info = info

class Node():
    def __init__(self, data):
        self.data = data
        self.firstarc = None

class GraphAdj():
    def __init__(self, v, a, vexs, arc, k="unorder"):
        self.vexnum = v
        self.arcnum = a 
        self.kind = k
        self.vexs = [Node(i) for i in vexs]

    def find(self, k):
        for i in range(self.vexnum):
            if self.vexs[i].data == k:
                return i
        else:
            return -1

# 创建无向图
def createUDG(v, a, vexs, arc):
    g = GraphAdj(v, a, vexs, arc)
    for t in arc:
        tmpi, tmpj = t
        i, j = g.find(tmpi), g.find(tmpj)
        newarci = Arc(j)
        newarci.next = g.vexs[i].firstarc
        g.vexs[i].firstarc = newarci

        newarcj = Arc(i)
        newarcj.next = g.vexs[j].firstarc
        g.vexs[j].firstarc = newarcj
    return g

# 深度优先搜索-中序遍历
def dfsTraversal(g):
    visit = [0] * g.vexnum
    linkset = []

    def dfs(g, i):
        visit[i] = 1
        linkset[-1].append(g.vexs[i].data)
        p = g.vexs[i].firstarc
        while p:
            if visit[p.adj] == 0:
                dfs(g, p.adj)
            p = p.next

    for i in range(g.vexnum):
        if visit[i] == 0:
            linkset.append([])
            dfs(g, i)

    print(linkset)
# 广度优先搜索-层序遍历
def bfsTraversal(g):
    visit = [0] * g.vexnum
    queue = []
    queue.append(g.vexs[0])
    while len(queue) != 0:
        p = queue.pop(0)
        index = g.find(p.data)
        if visit[index] == 0:
            print(p.data)
            visit[index] = 1
            q = p.firstarc
            while q:
                queue.append(g.vexs[q.adj])
                q = q.next

vexs = list(range(8))
arc = [[0, 7], [0, 1], [2, 0], [4, 1], [2, 4], [3, 5]]
g = createUDG(8, 6, vexs, arc)
dfsTraversal(g)
bfsTraversal(g)