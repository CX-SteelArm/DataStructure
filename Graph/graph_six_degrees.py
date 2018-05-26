# 六度空间问题
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

# 广度优先搜索-层序遍历
def sds(g):
    n = g.vexnum
    for i in range(n):
        count = bfsTraversal(g, i)
        print("{:d}: {:.2f}%".format(g.vexs[i].data, count/n*100))

def bfsTraversal(g, v):
    visit = [0] * g.vexnum
    visit[v] = 1
    queue = []
    queue.append(v)
    level, count = 0, 1
    tail, last = v, v
    while len(queue) != 0:
        p = queue.pop(0)
        q = g.vexs[p].firstarc
        while q:
            if visit[q.adj] == 0:
                visit[q.adj] = 1
                queue.append(q.adj)
                count += 1
                tail = q.adj
            if not q.next:
                break
            else:
                q = q.next
                
        if p == last:
            level += 1
            last = tail
        if level == 6:
            break
    return count

def getInput():
    x, n = 0, 0
    cro = []
    while True:
        s = input().split(" ")
        i, j = [eval(k) for k in s]
        if n == 0:
            x, n = i, j
            count = n
        else:
            cro.append([i, j])
            count -= 1
            if count == 0:
                break
    return x, n, cro

x, n, cro = getInput()
g = createUDG(x, n, list(range(1,x+1)), cro)
sds(g)

