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

# 层序遍历e元素，找到与其距离不同的层次上的节点
def minDistance(g, e):
    i = g.locateVex(e)
    visit = [0] * g.vexnum
    queue = []
    dis_list = []; tmp_list = [] # 记录不同层次节点的列表

    # 插入及访问第一个元素e
    queue.append(i)
    visit[i] = 1
    dis_list.append([g.vexs[i]])

    # 定义与层序遍历首尾相关的量
    level = 0; last = i; tail = i
    
    while len(queue) != 0:
        p = queue.pop(0)
        neighbor = []
        for j in range(g.vexnum):
            if g.adjmx[p][j] != 0:
                neighbor.append(j)
        for j in neighbor:
            if visit[j] == 0:
                visit[j] = 1
                tmp_list.append(g.vexs[j])
                tail = j
                queue.append(j)
        if p == last:
            level += 1
            last = tail
            if len(tmp_list) != 0:
                dis_list.append(tmp_list.copy())
                tmp_list = []
    
    return dis_list

vexs = ['A', 'B', 'C', 'D', 'E']
arc = [['A', 'C'], ['C', 'D'], ['E', 'D'], ['D', 'B']]
g = createGraph(5, 4, vexs, arc, "unorder")

print(minDistance(g, 'A'))