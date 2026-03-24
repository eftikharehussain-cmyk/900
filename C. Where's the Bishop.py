t = int(input())
for _ in range(t):
    line = input()
    while line == "":
        line = input()

    _mat = [line]
    for i in range(7):
        _mat.append(input())
    for i in range(1, len(_mat)-1):
        for j in range(1, len(_mat[i])-1):
            if _mat[i][j] == "#":
                if (_mat[i-1][j-1] == "#" and
                    _mat[i-1][j+1] == "#" and
                     _mat[i+1][j-1] == "#" and
                      _mat[i+1][j+1] == "#"):
                    print(i+1, j+1)