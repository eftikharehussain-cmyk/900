for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = [x for x in map(int, input().split())]
    _out = ""
    cnt = 0
    for i in range(len(lst)):
        if cnt + lst[i] <= k:
            cnt += lst[i]
            _out += str(1)
        else:
            cnt = cnt
            _out += str(0)
    print(_out)
