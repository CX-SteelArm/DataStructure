def createNode(l, r):
    c = {}
    c["left"] = l
    c["right"] = r
    return c

def buildTree(q):
    tree = []
    check = set()
    for i in q:
        l, r = i
        if l != '-':
            l = int(l)
            check.add(l)
        else:
            l = -1

        if r != '-':
            r = int(r)
            check.add(r)
        else:
            r = -1

        tree.append(createNode(l, r))

    head = set(range(len(q))) - check
    return tree, head.pop()

# 层序遍历
def inq(q, x):
    q.append(x)

def delq(q):
    return q.pop(0)

def levelOrderTraversal(tree, head):
    queue = [head]
    leaves = []
    while len(queue) != 0:
        t = queue[0]
        if tree[t]["left"] != -1:
            inq(queue, tree[t]["left"])
        if tree[t]["right"] != -1:
            inq(queue, tree[t]["right"])
        k = delq(queue)
        if tree[k]["left"] == -1 and tree[k]["right"] == -1:
            leaves.append(k)
    return leaves


from re import findall

def getInput():
    n = eval(input())
    q = []
    for i in range(n):
        nstr = input()
        nlist = tuple(findall("[0-9]+|-", nstr))
        q.append(nlist)
    return q

tree, head = buildTree(getInput())
leaves = levelOrderTraversal(tree, head)
print(" ".join([str(i) for i in leaves]))