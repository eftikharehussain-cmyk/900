_mat = []
for _ in range(3):
    _mat.append(list(map(int, input().split())))
first = [[1]*3 for _ in range(3)]
def toggle(i, j):
    if 3>i>=0 and 3>j>=0:
        first[i][j] = 1-first[i][j]

for i in range(3):
    for j in range(3):
        if _mat[i][j] % 2 != 0:
            toggle(i,j)
            toggle(i-1,j)
            toggle(i+1,j)
            toggle(i,j+1)
            toggle(i,j-1)
for row in first:
    print("".join(map(str,row)))