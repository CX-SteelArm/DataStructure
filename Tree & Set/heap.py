class Heap():
    def __init__(self, l=[], maxlen=100, maxData=1000):
        self.ele = [maxData]*maxlen
        self.size = 0
        self.buildHeap(l)

    def buildHeap(self, l):
        for i in l:
            self.insert(i)

    def insert(self, x):
        self.size += 1
        i = self.size
        while x > self.ele[i // 2]:
            self.ele[i] = self.ele[i//2]
            i = i // 2
        self.ele[i] = x

    def deleteMax(self):
        maxData = self.ele[0]
        temp = self.ele[self.size]
        self.size -= 1
        parent = 1
        while parent*2 <= self.size:
            child = parent * 2
            if child != self.size and self.ele[child] < self.ele[child+1]:
                child += 1
            if temp >= self.ele[child]:
                break
            else:
                self.ele[parent] = self.ele[child]
            parent = child
        self.ele[parent] = temp
        return maxData

    def printSelf(self):
        for i in range(1, self.size+1):
            print(self.ele[i], end=" ")

# h = Heap([5,6,3,0,8,9,7,1,2])
# h.delete()
# h.printSelf()

# 建造最大堆
class PerkHeap():
    def __init__(self, l, maxData=1000):
        self.ele = [maxData] + l
        self.size = len(l)

    def printSelf(self):
        for i in range(1,self.size+1):
            print(self.ele[i], end=" ")

def percDown(h, i):
    tmp = h.ele[i]
    while i*2 <= h.size:
        child = i*2
        if child != h.size and h.ele[child] < h.ele[child+1]:
            child += 1
        if tmp < h.ele[child]:
            h.ele[i] = h.ele[child]
        else:
            break
        i = child
    h.ele[i] = tmp

def buildHeap(h):
    for i in range(h.size // 2, 0, -1):
        percDown(h, i)

h = PerkHeap([4,2,3,1,5,0,9,8,7,6])
h.printSelf()
print("")
buildHeap(h)
h.printSelf()