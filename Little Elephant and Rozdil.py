n = int(input())
lst = [x for x in map(int, input().split())]
_min = min(lst)
cnt = lst.count(_min)
if cnt > 1:
    print("Still Rozdil")
else:
    _index = lst.index(min(lst))
    print(_index + 1)