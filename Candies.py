for _ in range(int(input())):
    n = int(input())
    a = [x for x in map(int, input().split())]
    _dict = {}
    for i in range(len(a)):
        if a[i] not in _dict:
            _dict[a[i]] = 1
        else:
            _dict[a[i]] += 1
    cnt = 0
    for key in _dict:
        if _dict[key] > 2:
            cnt += 1
    if cnt > 0:
        print("NO")
    else:
        print("YES")
