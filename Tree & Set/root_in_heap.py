class Heap():
    def __init__(self, l=[], maxlen=1000, minData=-10001):
        self.ele = [minData]*maxlen
        self.size = 0
        self.buildHeap(l)

    def buildHeap(self, l):
        for i in l:
            self.insert(i)

    def insert(self, x):
        self.size += 1
        i = self.size
        while x < self.ele[i // 2]:
            self.ele[i] = self.ele[i//2]
            i = i // 2
        self.ele[i] = x

    def printRoot(self, i):
        out = []
        while i != 0:
            out.append(str(self.ele[i]))
            i = i // 2
        print(" ".join(out))

    def printSelf(self):
        for i in range(1, self.size+1):
            print(self.ele[i], end=" ")

def getInput():
    N = 0; M = 0; h = None
    for i in range(3):
        s = input()
        tmp = [eval(i) for i in s.split(" ")]
        if i == 0:
            N, M = tmp
        elif i == 1:
            h = Heap(tmp)
        else:
            for j in tmp:
                h.printRoot(j)

getInput()


    
    