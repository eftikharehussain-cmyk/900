_mat = []
for _ in range(8):
    _mat.append(input())
white = black = 0
for i in range(len(_mat)):
    for j in range(len(_mat[i])):
        if _mat[i][j] == "Q":
            white += 9
        elif _mat[i][j] == "q":
            black += 9
        elif _mat[i][j] == "R":
            white += 5
        elif _mat[i][j] == "r":
            black += 5
        elif _mat[i][j] == "B":
            white += 3
        elif _mat[i][j] == "b":
            black += 3
        elif _mat[i][j] == "N":
            white += 3
        elif _mat[i][j] == "n":
            black += 3
        elif _mat[i][j] == "P":
            white += 1
        elif _mat[i][j] == "p":
            black += 1
if black == white:
    print("Draw")
elif white > black:
    print("White")
else:
    print("Black")