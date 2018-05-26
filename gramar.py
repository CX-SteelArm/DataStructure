
def foo(a):
    if a[-1] == 4:
        t = True
        return t
    else:
        k = foo(a[:-1])
        return k

print(foo([1,2,3,4,5,6,7,0]))