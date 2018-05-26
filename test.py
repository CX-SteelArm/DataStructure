minnum = 0; maxnum = 9999; tmp = maxnum; ERROR = -1
nlist = [39, 101, 45, 63, 44]
for i in nlist:
    if i > minnum and i < maxnum:
        if i > tmp:
            maxnum = i
        else:
            minnum = i
            maxnum if i > tmp else minnum = i
        tmp = i
    else:
        print(ERROR)
        break

