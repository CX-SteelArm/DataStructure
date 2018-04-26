class Node:

    def __init__(self, c, e):
        self.coef = c
        self.expon = e
        self.link = None

class LinkList:

    def __init__(self):
        self.head = Node(0, 0)

    def makeEmpty(self):
        pass

    def findKth(self, i):
        pass

    def insert(self, i, n):
        if i < 0 or i > self.length():
            self.error("insert out of range.")
            return -1;

        p = self.head
        for j in range(i):
            p = p.link
        n.link = p.link
        p.link = n

    def delete(self, i):
        if i < 0 or i >= self.length():
            self.error("delete out of range.")
            return -1;

        p = self.head
        for j in range(i):
            p = p.link
        k = p.link.link
        del p.link
        p.link = k

    def length(self):
        p = self.head
        i = -1
        while p:
            p = p.link
            i += 1
        return i

    def prtSelf(self):
        p = self.head.link
        if p:
            s = ""
            while p:
                s += "{} {} ".format(p.coef, p.expon)
                p = p.link
            print(s[:-1], end="")
        else:
            print("0 0", end="")

    def error(self, s):
        print("Warning! " + s)

    def popZero(self):
        p = self.head.link
        i = 0
        while p:
            if p.coef == 0:
                self.delete(i)
            else:
                i += 1
            p = p.link


# l = LinkList()
# l.insert(0, Node(1,1))
# l.insert(l.length(), Node(2,2))
# l.prtSelf()

from re import findall

def attach(nlist):
    l = LinkList()
    for i in range(len(nlist)//2):
        newNode = Node(nlist[i*2+1], nlist[i*2+2])
        l.insert(l.length(), newNode)
    return l

def getInput():
    nstr1 = input()
    nlist1 = [int(i) for i in findall('-?\w+', nstr1)]

    nstr2 = input()
    nlist2 = [int(i) for i in findall('-?\w+', nstr2)]

    p1 = attach(nlist1)
    p2 = attach(nlist2)
    return p1, p2

def polynomialAdd(p1, p2):
    t1 = p1.head.link
    t2 = p2.head.link
    t = LinkList()

    while t1 and t2:
        if t1.expon == t2.expon:
            newNode = Node(t1.coef + t2.coef, t1.expon)
            if newNode.coef == 0:
                del newNode
            else:
                t.insert(t.length(), newNode)
            t1 = t1.link
            t2 = t2.link

        elif t1.expon > t2.expon:
            newNode = Node(t1.coef, t1.expon)
            if newNode.coef == 0:
                del newNode
            else:
                t.insert(t.length(), newNode)
            t1 = t1.link

        else:
            newNode = Node(t2.coef, t2.expon)
            t.insert(t.length(), newNode)
            t2 = t2.link

    while t1:
        newNode = Node(t1.coef, t1.expon)
        t.insert(t.length(), newNode)
        t1 = t1.link

    while t2:
        newNode = Node(t2.coef, t2.expon)
        t.insert(t.length(), newNode)
        t2 = t2.link

    t.popZero()
    t.prtSelf()

def polynomialMul(p1, p2):
    t1 = p1.head.link
    t2 = p2.head.link
    t = LinkList()

    while t2:
        newNode = Node(t1.coef * t2.coef, t1.expon + t2.expon)
        t.insert(t.length(), newNode)
        t2 = t2.link

    if t.length == 0:
        t.insert(0, Node(0, 0))

    t1 = t1.link
    while t1:
        t2 = p2.head.link
        t_ = t.head.link
        while t2:
            newNode = Node(t1.coef * t2.coef, t1.expon + t2.expon)

            while t_.link and t_.link.expon > newNode.expon:
                t_ = t_.link

            if t_.link and t_.link.expon == newNode.expon:
                t_.link.coef += newNode.coef

            elif newNode.coef != 0:
                newNode.link = t_.link
                t_.link = newNode
            t2 = t2.link
        t1 = t1.link

    t.popZero()
    t.prtSelf()

# for test
# 0 0 5 0 4 1 3
# 4 3 4 -5 2  6 1  -2 0
# 3 5 20  -7 4  3 1

p1, p2 = getInput()
polynomialMul(p1, p2)
print("")
polynomialAdd(p1, p2)