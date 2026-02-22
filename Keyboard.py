_mat = [['q','w','e','r','t','y','u','i','o','p'],
        ['a','s','d','f','g','h','j','k','l',';'],
        ['z','x','c','v','b','n','m',',','.','/']]
a = input()
b = input().strip()
_chr = ""

for i in range(len(b)):
    for j in range(len(_mat)):
        for k in range(len(_mat[j])):
            if b[i] == _mat[j][k]:
                if a == "R":
                    _chr +=_mat[j][k-1]
                else:
                    _chr +=_mat[j][k + 1]

print(_chr)