for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    _mat = []
    for _ in range(len(lst)):
        k, m = input().split()
        _mat.append(m)
    for i in range(len(lst)):
        for j in range(len(_mat[i])):
            if _mat[i][j] == "D":
                if lst[i] < 9:
                    lst[i] += 1
                else:
                    lst[i] = 0
            elif _mat[i][j] == "U":
                if lst[i] > 0:
                    lst[i] -= 1
                elif lst[i] == 0:
                    lst[i] = 9
    print(*lst)
