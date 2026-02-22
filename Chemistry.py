for _ in range(int(input())):
    n, k = map(int, input().split())
    _str = input()
    lst = list(_str)
    _dict = {}
    for i in range(n):
        if lst[i] not in _dict:
            _dict[lst[i]] = 1
        else:
            _dict[lst[i]] += 1
    _lst1 = []
    _lst2 = []
    for key, value in _dict.items():
        if value % 2 != 0:
            _lst1.append(value)
        else:
            _lst2.append(value)
    if (k+1) >= len(_lst1):
        print("yes")
    else:
        print("no")