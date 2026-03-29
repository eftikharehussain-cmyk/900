na, nb = map(int, input().split())
k, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
if a[k-1] < b[nb-m]:
    print("YES")
else:
    print("NO")