# 使用dict和list构建二叉树

def createNode(d, l, r):
    c = {}
    c["data"] = d
    c["left"] = l
    c["right"] = r
    return c

def buildTree(q):
    tree = []
    check = set()
    for i in q:
        d, l, r = i
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

        tree.append(createNode(d, l, r))

    head = set(range(len(q))) - check
    return tree, head.pop()

tree, head = buildTree([('A', '1', '2'), ('C', '3', '4'), ('B', '-', '-'), ('E', '-', '5'), ('D', '6', '-'), ('G', '-', '-'), ('F', '-', '-')])
print(tree)

# 先序/中序/后序遍历
def preOrderTraversal(tree, head):
    if head == -1:
        return 0
    else:
        print(tree[head]["data"], end=" ")
        preOrderTraversal(tree, tree[head]["left"])
        preOrderTraversal(tree, tree[head]["right"])

def inOrderTraversal(tree, head):
    if head == -1:
        return 0
    else:
        inOrderTraversal(tree, tree[head]["left"])
        print(tree[head]["data"], end=" ")
        inOrderTraversal(tree, tree[head]["right"])

def postOrderTraversal(tree, head):
    if head == -1:
        return 0
    else:
        postOrderTraversal(tree, tree[head]["left"])
        postOrderTraversal(tree, tree[head]["right"])
        print(tree[head]["data"], end=" ")

# 不使用递归实现先序/中序/后序遍历
def isNotEmpty(x):
    return len(x) != 0
def push(s, x):
    s.append(x)
def pop(s):
    return s.pop()

def inorder(tree, head):
    stack = []
    t = head
    while t != -1 or isNotEmpty(stack):
        while t != -1:
            push(stack, t)
            t = tree[t]["left"]

        if isNotEmpty(stack):
            t = pop(stack)
            print(tree[t]["data"], end=" ")
            t = tree[t]["right"]

def preorder(tree, head):
    stack = []
    t = head
    while t != -1 or isNotEmpty(stack):
        while t != -1:
            print(tree[t]["data"], end=" ")
            push(stack, t)
            t = tree[t]["left"]

        if isNotEmpty(stack):
            t = pop(stack)
            t = tree[t]["right"]

def postorder(tree, head):
    stack = []
    visit = [0] * len(tree)
    t = head
    while t != -1 or isNotEmpty(stack):
        while t != -1:
            push(stack, t)
            visit[t] += 1
            t = tree[t]["left"]

        if isNotEmpty(stack):
            t = pop(stack)
            if visit[t] == 2:
                print(tree[t]["data"], end=" ")
                t = -1
            else:
                push(stack, t)
                visit[t] += 1
                t = tree[t]["right"]

# 层序遍历
inq = push
def delq(q):
    return q.pop(0)


def levelOrderTraversal(tree, head):
    queue = [head]
    while len(queue) != 0:
        t = queue[0]
        if tree[t]["left"] != -1:
            inq(queue, tree[t]["left"])
        if tree[t]["right"] != -1:
            inq(queue, tree[t]["right"])
        print(tree[delq(queue)]["data"], end=" ")

preOrderTraversal(tree, head)
print("")
inOrderTraversal(tree, head)
print("")
postOrderTraversal(tree, head)
print("\n-------------")
preorder(tree, head)
print("")
inorder(tree, head)
print("")
postorder(tree, head)
print("\n-------------")
levelOrderTraversal(tree, head)