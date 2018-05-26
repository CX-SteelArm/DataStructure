# 邻接多重表，用以处理无向链表删除弧或标记的问题

class Node():
    def __init__(self, data):
        self.data = data
        self.firstedge = None

class Arc():
    def __init__(self, ivex, jvex, ilink, jlink, info=None):
        self.ivex = ivex
        self.jvex = jvex
        self.info = info
        self.ilink = ilink
        self.jlink = jlink

class Graph():
    def __init__(self, v, a, vexs, arc):
        self.vexnum = v
        self.arcnum = a 
        self.vexs = [Node(i) for i in vexs]
        self.kind = "unorder"

    def find(self, k):
        for i in range(self.vexnum):
            if self.vexs[i].data == k:
                return i
        else:
            return -1

def createUDG(v, a, vexs, arc):
    g = Graph(v, a, vexs, arc)
    for t in arc:
        tmpi, tmpj = t
        i, j = g.find(tmpi), g.find(tmpj)
        # 十字链表的方法
        ac = Arc(i, j, g.vexs[i].firstedge, g.vexs[j].firstedge)
        g.vexs[i].firstedge = ac
        g.vexs[j].firstedge = ac
    return g

vexs = ['A', 'B', 'C', 'D', 'E']
arc = [['A', 'C'], ['C', 'D'], ['D', 'E'], ['D', 'B']]
g = createUDG(5, 4, vexs, arc)


# 遍历顺序存在一些不同
def traversal(g):
    visit = [0] * g.vexnum
    def fs(ar):
        if not ar:
            return
        m, n = ar.ivex, ar.jvex
        for j in [m, n]:
            if visit[j] == 0:
                print(g.vexs[j].data)
                visit[j] = 1
        fs(ar.ilink)
        fs(ar.jlink)

    for i in range(g.vexnum):
        fs(g.vexs[i].firstedge)

traversal(g)