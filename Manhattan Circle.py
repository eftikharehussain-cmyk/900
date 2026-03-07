for _ in range(int(input())):
    _mat = []
    n, m = map(int, input().split())
    for _ in range(n):
        _mat.append(input())
    cnt = 0
    cnt1 = 0
    for i in range(len(_mat)):
        s = _mat[i].count("#")
        if s > cnt:
            cnt = s
            cnt1 = i
        elif s < cnt:break
    lst = []
    for j in range(len(_mat[cnt1])):
        if _mat[cnt1][j] == "#":
            lst.append(j+1)
    lenght = (len(lst))//2
    print( cnt1+1, lst[lenght])
