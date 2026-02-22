n = int(input())
if n > 0 or n == 0:
    print(n)
else:
    t = str(n)
    lst = list(t)
    lst1 = lst[:]
    t1 = lst.pop(-1)
    tot = "".join(lst)
    t2 = lst1.pop(-2)
    tot1 = "".join(lst1)
    tot = int(tot)
    tot1 = int(tot1)
    print(max(tot, tot1))