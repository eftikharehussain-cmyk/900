for _ in range(int(input())):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    _dict = {}
    for i in lst:
        if i not in _dict:
            _dict[i] = 1
        else:
            _dict[i] += 1
    lst1 = []
    for key in _dict:
        if _dict[key] % 2 != 0:
            lst1.append(key)
    for j in lst1:
        print(j)