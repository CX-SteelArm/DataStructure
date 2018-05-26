# 使用邻接表存储图，对稀疏关系很好

class Arc():
    def __init__(self, adj, info=None):
        self.adj = adj
        self.next = None
        self.info = info

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

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
        p = g.vexs[i]
        while p.next and p.next.adj < j:
            p = p.next
        newarci.next = p.next
        p.next = newarci

        newarcj = Arc(i)
        p = g.vexs[j]
        while p.next and p.next.adj < i:
            p = p.next
        newarcj.next = p.next
        p.next = newarcj
    return g


# 深度优先搜索-中序遍历
def dfsTraversal(g):
    visit = [0] * g.vexnum
    setlist = []

    def dfs(g, i):
        visit[i] = 1
        setlist[-1].append(g.vexs[i].data)
        p = g.vexs[i].next
        while p:
            if visit[p.adj] == 0:
                dfs(g, p.adj)
            p = p.next

    for i in range(g.vexnum):
        if visit[i] == 0:
            setlist.append([])
            dfs(g, i)
    
    for t in setlist:
        print("{ " + " ".join([str(i) for i in t]) + " }")

# 广度优先搜索-层序遍历
def bfsTraversal(g):
    visit = [0] * g.vexnum
    queue = []
    setlist = []

    for i in range(g.vexnum):
        flag = 0
        queue.append(g.vexs[i])
        while len(queue) != 0:
            p = queue.pop(0)
            index = g.find(p.data)
            if visit[index] == 0:
                if flag == 0:
                    setlist.append([])
                    flag = 1
                setlist[-1].append(index)
                visit[index] = 1
                q = p.next
                while q:
                    queue.append(g.vexs[q.adj])
                    q = q.next
    for t in setlist:
        print("{ " + " ".join([str(i) for i in t]) + " }")

def getInput():
    n, x = 0, 1
    vexs, arc = [], []
    while x != 0:
        s = input().split(" ")
        i, j = [eval(k) for k in s]
        if n == 0:
            n, x = i, j
            vexs = list(range(n))
        else:
            arc.append([i, j])
            x -= 1
    g = createUDG(n, x, vexs, arc)
    dfsTraversal(g)
    bfsTraversal(g)

# vexs = list(range(8))
# arc = [[0, 7], [0, 1], [2, 0], [4, 1], [2, 4], [3, 5]]
# g = createUDG(8, 6, vexs, arc)
# dfsTraversal(g)
# bfsTraversal(g)

getInput()