def createNode(d, l, r):
    c = {}
    c["data"] = d
    c["left"] = l
    c["right"] = r
    return c

def buildTree(q):
    tree = []
    check = set()
    for i in q:
        d, l, r = i
        if l != '-':
            l = int(l)
            check.add(l)
        else:
            l = -1

        if r != '-':
            r = int(r)
            check.add(r)
        else:
            r = -1

        tree.append(createNode(d, l, r))

    head = set(range(len(q))) - check
    if len(head) == 0:
        return tree, -1
    else:
        return tree, head.pop()

def isOmorphic(tree1, tree2, head1, head2):
    if head1 == -1 and head2 == -1:
        return True
    if head1 == -1 and head2 != -1:
        return False
    if tree1[head1]["data"] != tree2[head2]["data"]:
        return False
    if tree1[head1]["left"] == -1 and tree2[head2]["left"] == -1:
        return isOmorphic(tree1, tree2, tree1[head1]["right"], tree2[head2]["right"])
    if tree1[head1]["left"] != -1 and tree2[head2]["left"] != -1 and tree1[tree1[head1]["left"]]["data"] == tree2[tree2[head2]["left"]]["data"]:
        return isOmorphic(tree1, tree2, tree1[head1]["left"], tree2[head2]["left"]) and isOmorphic(tree1, tree2, tree1[head1]["right"], tree2[head2]["right"])
    else:
        return isOmorphic(tree1, tree2, tree1[head1]["left"], tree2[head2]["right"]) and isOmorphic(tree1, tree2, tree1[head1]["right"], tree2[head2]["left"])

# tree1, head1 = buildTree([('A', '1', '2'), ('C', '3', '4'), ('B', '-', '-'), ('E', '-', '5'), ('D', '6', '-'), ('G', '-', '-'), ('F', '-', '-')])
# tree2, head2 = buildTree([('A', '1', '2'), ('C', '3', '4'), ('B', '-', '-'), ('E', '-', '5'), ('D', '6', '-'), ('G', '-', '-'), ('F', '-', '-')])

# print(isOmorphic(tree1, tree2, head1, head2))

from re import findall

def getInput():
    n = eval(input())
    q = []
    for i in range(n):
        nstr = input()
        nlist = tuple(findall("[A-Z0-9]+|-", nstr))
        q.append(nlist)
    return q

tree1, head1 = buildTree(getInput())
tree2, head2 = buildTree(getInput())

print("YES") if isOmorphic(tree1, tree2, head1, head2) else print("NO")