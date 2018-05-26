def root(plist):
    l = len(plist)
    if l == 0:
        return -1
    if l == 1:
        return 0
    i = 0
    while True:
        if 2**(i+1)-1 >= l:
            break
        i += 1
    restl = l - (2**i - 1)
    restright = restl - 2**(i-1)
    if restright < 0:
        restright = 0
    restleft = restl - restright
    # print(restleft, restright)
    center = restleft + (l-restleft-restright-1) // 2
    return center

class Node():
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

def comAVL(plist):
    r = root(plist)
    if r == -1:
        return None

    n = Node(plist[r])
    if len(plist) == 1:
        pass
    else:
        left = plist[:r]
        right = plist[r+1:]
        n.left = comAVL(left)
        n.right = comAVL(right)
    return n

def levelTraversal(n):
    queue = []
    out = []
    queue.append(n)
    while len(queue) != 0:
        t = queue[0]
        if t.left:
            queue.append(t.left)
        if t.right:
            queue.append(t.right)
        out.append(str(queue.pop(0).value))
    print(" ".join(out))


def getInput():
    input()
    q = input()
    qlist = [eval(i) for i in q.split(" ")]
    qlist.sort()
    n = comAVL(qlist)
    levelTraversal(n)

getInput()