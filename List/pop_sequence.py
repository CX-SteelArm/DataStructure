
def checkPop(list_pop, M, N):
    stack = []
    cur = 0

    for j in list_pop:
        while j > cur:
            cur += 1
            stack.append(cur)
        if len(stack) > M:
            return "NO"

        k = stack.pop()
        if k != j:
            return "NO"

    return "YES"

from re import findall

def getInput():
    m = input()
    M, N, k = [int(i) for i in findall('-?\w+', m)]
    result = []
    for i in range(k):
        nstr = input()
        nlist = [int(i) for i in findall('-?\w+', nstr)]
        result.append(checkPop(nlist, M, N))

    for i in result:
        print(i)

getInput()