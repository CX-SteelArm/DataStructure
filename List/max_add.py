# Max sum of the subcolumns
# Algorithm 1 ~ O(N^3)
def al1(nlist):

    maxSum = 0
    l = len(nlist)

    for i in range(l):
        for j in range(i, l):
            sum = 0;
            for k in range(j,l):
                sum += nlist[k]
                if sum > maxSum:
                    maxSum = sum

    return maxSum

# Algorithm 2 ~ O(N^2)
def al2(nlist):

    maxSum = 0
    l = len(nlist)

    for i in range(l):
        sum = 0
        for j in range(i, l):
            sum += nlist[j];
            if sum > maxSum:
                maxSum = sum
    
    return maxSum

# Algorithm 3 ~ O(Nlg(N))
def al3(nlist, left=None, right=None):

    maxSum = 0
    l = len(nlist)

    if left == None:
        left = 0

    if right == None:
        right = l-1

    center = (left + right) // 2
    if left == right:
        return 0;

    maxleft = al3(nlist, left, center)
    maxright = al3(nlist, center+1, right)

    leftBorderSum = 0
    maxLeftSum = 0
    for i in range(center,-1,-1):
        leftBorderSum += nlist[i];
        if leftBorderSum > maxLeftSum:
            maxLeftSum = leftBorderSum

    rightBorderSum = 0
    maxRightSum = 0
    for i in range(center+1, right+1):
        rightBorderSum += nlist[i];
        if rightBorderSum > maxRightSum:
            maxRightSum = rightBorderSum

    return max(maxleft, maxright, maxLeftSum + maxRightSum);

# Algorithm 4 ~ O(N)
def al4(nlist):
    sum = 0
    maxSum = 0
    l = len(nlist)

    for i in range(l):
        sum += nlist[i]
        if sum < 0:
            sum = 0
        
        if sum > maxSum:
            maxSum = sum

    return maxSum

'''
from random import randint
nlist = []
for i in range(10):
    nlist.clear()
    n = randint(20,40)
    for j in range(n):
        nlist.append(randint(-9, 20))
    print("Random list:", nlist)
    print("result:", al1(nlist), al2(nlist), al3(nlist), al4(nlist))
'''
from re import findall

def getInput():
    n = input()
    nstr = input()
    nlist = [int(i) for i in findall('-?\w+', nstr)]
    print(al1(nlist), al2(nlist), al3(nlist), al4(nlist))

getInput()