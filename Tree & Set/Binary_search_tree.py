class Node():
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

def buildBST(l=[]):
    t = None
    for i in l:
        t = insert(i, t)
    return t

def findInBST(x, t):
    p = t
    while p != None:
        if p.value < x:
            p = p.right
        elif p.value > x:
            p = p.left
        else:
            return True
    return False

def findMin(t):
    p = t
    while p.left != None:
        p = p.left
    return p.value

def findMax(t):
    p = t
    while p.right != None:
        p = p.right
    return p.value

def insert(x, t):
    # 递归
    if t == None:
        t = Node(x)
    else:
        if x < t.value:
            t.left = insert(x, t.left)
        elif x > t.value:
            t.right = insert(x, t.right)
    return t
    

def delete(x, t):
    # 重要的操作，使用递归实现较清晰，return t访问上级节点，实际上是栈的思想
    if t == None:
        print("not found")
    elif x < t.value:
        t.left = delete(x, t.left)
    elif x > t.value:
        t.right = delete(x, t.right)
    else:
        if t.left and t.right:
            tmp = findMin(t)
            t.value = tmp
            t.right = delete(tmp, t.right)
        else:
            tmp = t
            if t.left == None:
                t = t.right
            elif t.right == None:
                t = t.left
            del tmp
    return t

def printSelf(t):
    # 层序遍历打印树
    if t == None:
        print("Empty tree")
        return

    queue = []
    queue.append(t)

    while len(queue) != 0:
        p = queue[0]
        if p.left != None:
            queue.append(p.left)
        if p.right != None:
            queue.append(p.right)
        print(p.value, end=" ")
        queue.remove(p)

# b = buildBST([4,5,1,2,3,5,6])
# printSelf(b)
# print(findInBST(1, b))
# delete(1, b)
# print(findInBST(1, b))
# printSelf(b)



