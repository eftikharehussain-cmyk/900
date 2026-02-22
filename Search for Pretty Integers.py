n, m = map(int, input().split())
a = [x for x in map(int, input().split())]
b = [x for x in map(int, input().split())]
lst = []
for i in a:
    if i in b:
        lst.append(i)
if len(lst) == 0:
    _min_a = min(a)
    _min_b = min(b)
    if _min_a == _min_b:
        print(_min_a)
    else:
        if _min_a > _min_b:
            print(str(_min_b) + str(_min_a))
        else:
            print(str(_min_a) + str(_min_b))
else:
    print(min(lst))