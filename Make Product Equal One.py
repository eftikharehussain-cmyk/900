n = int(input())
a = [int(x) for x in input().split()]
cnt = cnt1 = 0
h = 0
for i in a:
    if i > 1:
        t = i-1
        cnt += t
    elif i < 0 and i != -1:
        t = (abs(i)-1)
        cnt += t
        cnt1 += 1
    elif i == -1:
        cnt1 += 1
    elif i == 0:
        cnt += 1
        h += 1

if h == 0:
    if cnt1 % 2 != 0:
        cnt += 2
print(cnt)