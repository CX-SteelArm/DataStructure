def createSet(n):
    s = [-1] * n
    return s

# i是下标
def find(s, i):
    if s[i] < 0:
        return i
    else:
        i = find(s, s[i])
        return i

def connect(s, i, j):
    i = find(s, i)
    j = find(s, j)
    if i == j:
        return
    else:
        if -s[i] > -s[j]:
            s[j] = i
        elif -s[i] < -s[j]:
            s[i] = j
        else:
            s[j] = i
            s[i] -= 1

def check(s, i, j):
    i = find(s, i)
    j = find(s, j)
    if i == j:
        print("yes")
    else:
        print("no")

def checkCollect(s):
    i = sum(list(map(lambda x: 1 if x < 0 else 0, s)))
    print("The network is connected.") if i == 1 else print("There are {:d} components.".format(i))

def getInput():
    s = None;
    while True:
        t = input()
        if t[0].isdigit():
            s = createSet(eval(t))
        else:
            opr = t[0]
            if opr == 'S':
                checkCollect(s)
                break
            i, j = [eval(i) for i in t[2:].split(" ")]
            if opr == 'C':
                check(s, i-1, j-1)
            elif opr == 'I':
                connect(s, i-1, j-1)
                

getInput()