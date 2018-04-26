# Algorithm ~ O(N)
def al(nlist):
    l = len(nlist)
    currentSum = 0
    maxSum = 0
    left = nlist[0]
    right = nlist[-1]
    reserveL = left
    reserveR = right
    for i in range(l):
        currentSum += nlist[i]
        if currentSum < 0 and i <= l-2:
            currentSum = 0
            left = nlist[i+1]
            right = nlist[i+1]

        elif currentSum > maxSum or (maxSum == 0 and currentSum == maxSum):
            maxSum = currentSum
            right = nlist[i]
            reserveL = left
            reserveR = right

    return maxSum, reserveL, reserveR

from re import findall

def getInput():
    n = input()
    nstr = input()
    nlist = [int(i) for i in findall('-?\w+', nstr)]
    maxSum, left, right = al(nlist)
    print(maxSum, left, right)

getInput()