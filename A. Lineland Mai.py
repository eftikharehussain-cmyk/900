n = int(input())
a = [int(x) for x in input().split()]
t = a[0]
t1 = a[-1]
lst = []
lst1 = []
for i in range(len(a)):
    lst.append(max(abs(a[i] - t), abs(a[i]-t1)))
    if i == 0:
        lst1.append(abs(a[i] - a[i+1]))
    elif i == len(a)-1:
        lst1.append(abs(a[i]-a[i-1]))
    else:
        lst1.append(min(abs(a[i]-a[i+1]), abs(a[i]-a[i-1])))
_lst = []
for j in range(len(lst)):
    _lst.append([lst1[j], lst[j]])
for k in _lst:
    print(*k)