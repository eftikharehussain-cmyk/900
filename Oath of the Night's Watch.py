n = int(input())
a=[int(x) for x in input().split()]
_max = max(a)
_min = min(a)
cnt = 0
for i in a:
    if i != _max and i != _min:
        cnt += 1
print(cnt)