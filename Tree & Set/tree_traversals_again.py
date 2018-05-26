class Node():
    def __init__(self):
        self.left = -1
        self.right = -1
        self.visit = 0

from re import findall

def getInput():
    n = eval(input())
    s = []
    for i in range(n*2):
        nstr = input()
        s.append(nstr)
    return s

def buildTree(s):
    tree = [0]*(len(s)//2+1)
    stack = []
    t = -1
    for i in s:
        if i.startswith("Push"):
            j = eval(i[5:])
            stack.append(j)
            tree[j] = Node()
            if t == -1:
                t = tree[j]
                head = j
            elif t.visit == 0:
                t.left = j
                t = tree[j]
            else:
                t.right = j
                t = tree[j]
        elif i.startswith("Pop"):
            t = tree[stack.pop()]
            t.visit = 1
    return tree, head

s = getInput()
t, h = buildTree(s)

def postorder(tree, head):
    t = head
    stack = []
    visit = [0] * len(tree)
    outlist = []
    def isNotEmpty(s):
        return len(s) != 0
    while t != -1 or isNotEmpty(stack):
        while t != -1:
            stack.append(t)
            visit[t] += 1
            t = tree[t].left
            
        if isNotEmpty(stack):
            t = stack.pop()
            if visit[t] == 2:
                outlist.append(t)
                t = -1
            else:
                stack.append(t)
                visit[t] += 1
                t = tree[t].right
    return outlist

print(" ".join(str(i) for i in postorder(t, h)))
