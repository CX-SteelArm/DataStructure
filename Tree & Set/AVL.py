class Node():
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        self.height = 0
        self.flag = 0

def buildAVL(l=[]):
    t = None
    for i in l:
        t = insert(i, t)
    return t

def findInAVL(x, t):
    p = t
    while p != None:
        if p.value < x:
            p = p.right
        elif p.value > x:
            p = p.left
        else:
            return True
    return False

def getHeight(t):
    if not t:
        return -1
    return t.height

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
    print("")

def getHeight(a):
    if not a:
        return 0
    else:
        return a.height

def singleLeftRotation(a):
    b = a.left
    a.left = b.right
    b.right = a
    a.height = max(getHeight(a.left), getHeight(a.right)) + 1
    b.height = max(getHeight(b.left), getHeight(b.right)) + 1
    return b

def singleRightRotation(a):
    b = a.right
    a.right = b.left
    b.left = a
    a.height = max(getHeight(a.left), getHeight(a.right)) + 1
    b.height = max(getHeight(b.left), getHeight(b.right)) + 1
    return b

def doubleLeftRightRotation(a):
    # a-b-c 先b-c做一次单右旋 然后a-c做一次单左旋
    a.left = singleRightRotation(a.left)
    return singleLeftRotation(a)

def doubleRightLeftRotation(a):
    a.right = singleLeftRotation(a.right)
    return singleRightRotation(a)

def insert(x, t):
    if t == None:
        t = Node(x)
    else:
        if x < t.value:
            t.left = insert(x, t.left)
            if getHeight(t.left) - getHeight(t.right) == 2:
                if x < t.left.value:
                    t = singleLeftRotation(t)
                else:
                    t = doubleLeftRightRotation(t)

        elif x > t.value:
            t.right = insert(x, t.right)
            if getHeight(t.left) - getHeight(t.right) == -2:
                if x > t.right.value:
                    t = singleRightRotation(t)
                else:
                    t = doubleRightLeftRotation(t)
                
    t.height = max(getHeight(t.left), getHeight(t.right)) + 1
    return t

def clearFlag(t):
    if t:
        t.flag = 0
        clearFlag(t.left)
        clearFlag(t.right)

def check(x, t):
    if t.flag == 0:
        if x == t.value:
            t.flag = 1
            return 1
        else:
            return 0
    else:
        if x < t.value:
            return check(x, t.left)
        elif x > t.value:
            return check(x, t.right)
        else:
            return 0

def judge(l, t):
    clearFlag(t)
    for i in l:
        j = check(i, t)
        if j == 0:
            return "No"
    return "Yes"

def getInput():
    n = 0; l = 0; avl = None; out = []
    while True:
        s = input()
        list_s = [eval(i) for i in s.split()]
        if l == 0:
            avl = None
            n = list_s[0]
            if n > 10:
                n = 10
            elif n == 0:
                for j in out:
                    print(j)
                break
            else:
                l = list_s[1]
                
        else:
            if avl:
                out.append(judge(list_s, avl))
                l -= 1
            else:
                avl = buildAVL(list_s)
            
b = buildAVL([8,7,9,5,2,1,1,4,2,6,0,3])
printSelf(b)
# a = buildAVL([3,1,4,2])
# printSelf(a)
#getInput()