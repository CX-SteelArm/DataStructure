class Node:
    def __init__(self, d):
        self.data = d
        self.link = None

class LinkList:
    def __init__(self):
        self.head = Node(0)

    def makeEmpty(self):
        _node_list = []
        p = self.head.link
        while p:
            _node_list.append(p)
            p = p.link
        for i in _node_list:
            del i

    def findKth(self, i):
        if i < 0 or i > self.length():
            self.error("find out of range.")
            return error;

        p = self.head.link
        for j in range(i):
            p = p.link
        return p

    def insert(self, i, n):
        # insert as the i+1 th member
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
        r = p.link
        p.link = k
        return r

    def length(self):
        p = self.head
        i = -1
        while p:
            p = p.link
            i += 1
        return i

    def prtSelf(self):
        p = self.head.link
        s = ""
        while p:
            s += "{} ".format(p.data)
            p = p.link
        print(s, end=" ")

    def error(self, s):
        print("Warning! " + s)

class Stack(LinkList):
    def __init__(self):
        LinkList.__init__(self)

    def pop(self):
        return self.delete(self.length()-1)

    def push(self, n):
        self.insert(self.length(), n)

class Queue(LinkList):
    def __init__(self):
        LinkList.__init__(self)

    def enq(self):
        self.insert(self.length(), n)

    def delq(self):
        return self.delete(0)

'''
simple stack&queue using list
stack = []
stack.append --- push
stack.pop --- pop

queue = []
queue.append --- enq
queue.pop(0) --- delq
'''