_mat = []
for _ in range(int(input())):
    a, b = input().split()
    a[0].upper()
    a[1:].lower()
    _mat.append([a, b])
lst = []
for i in range(len(_mat)):
    if _mat[i][1] == "rat":
        _mat[i][1] = 1
    elif _mat[i][1] == "woman" or _mat[i][1] == "child":
        _mat[i][1] = 2
    elif _mat[i][1] == "man":
        _mat[i][1] = 3
    elif _mat[i][1] == "captain":
        _mat[i][1] = 4
_mat.sort(key=lambda x: x[1])
for k in _mat:
    print(k[0])

