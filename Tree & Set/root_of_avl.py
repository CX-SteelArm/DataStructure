class Node():
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        self.height = 0

def buildAVL(l=[]):
    t = None
    for i in l:
        t = insert(i, t)
    return t

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

def getInput():
    n = eval(input())
    s = input()
    list_s = [eval(i) for i in s.split()]
    b = buildAVL(list_s)
    print(b.value)

getInput()