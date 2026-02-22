n = int(input())
lst = list(map(int, input().split()))
lst1 = lst[:]
for i in range(n):
    lst1.append(lst1[i])
_max = 0
cnt = 1
cnt1 = lst1.count(1)
for i in range(len(lst1) -1):
    if lst1[i] == 1 and lst1[i+1] == 1:
        cnt += 1
        if cnt > _max:
            _max = cnt

    else:
        cnt = 1
if _max == 0 and cnt1 >= 1:
    _max = 1
print(_max)