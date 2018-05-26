# 拯救007，使用深度优先搜索方法
class StepNode():
    def __init__(self, cur, cho):
        self.current = cur
        self.choose = cho

class Node():
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.canJumpTo = None

def getInput():
    n, x = 1, 0
    count = 0
    cro = []
    while n != 0:
        s = input().split(" ")
        i, j = [eval(k) for k in s]
        if x == 0:
            n, x = i, j
        else:
            if i**2 + j**2 > 7.5**2 and abs(i) <= 50 and abs(j) <= 50:
                cro.append(Node(count, i, j))
                count += 1
            n -= 1
    return x, cro

def firstJump():
    if jump >= 50 - 7.5:
        return True
    else:
        ch = []
        for i in range(len(crocodiles)):
            if crocodiles[i].x**2 + crocodiles[i].y**2 <= (jump + radius)**2:
                ch.append(i)
        step.append(StepNode(-1, ch))

def dfsJump():
    def isSave(i):
        if 50-abs(i.x) <= jump or 50-abs(i.y) <= jump:
            return True
        else:
            return False

    jumpPath = []
    jumpTo = []
    k = False
    def dfs(i):
        nonlocal k
        if visit[i.index] == 0:
            visit[i.index] = 1
            if isSave(i):
                k = True
            else:
                ch = []
                for j in range(len(crocodiles)):
                    if (crocodiles[j].x-i.x)**2 + (crocodiles[j].y-i.y)**2 <= jump**2:
                        ch.append(j)
                i.canJumpTo = ch

                jumpTo.append(i.index)

                for j in i.canJumpTo:
                    k = dfs(crocodiles[j])
                    if k:
                        m = jumpTo.copy()
                        m.append(j)
                        jumpPath.append(m)
                        k = False
                else:
                    jumpTo.pop()
        return k

    for i in step[0].choose:
        if visit[i] == 0:
            k = dfs(crocodiles[i])
    return jumpPath


jump, crocodiles = getInput()
visit = [0] * len(crocodiles)
step = []
radius = 7.5

if firstJump():
    print(1)
else:
    jumpPath = dfsJump()
    if len(jumpPath) == 0:
        print(0)
    else:
        jumpPath.sort(key=len)
        # print(jumpPath)
        minPath = jumpPath[0]
        print(len(minPath)+1)
        for i in minPath:
            print(crocodiles[i].x, crocodiles[i].y)