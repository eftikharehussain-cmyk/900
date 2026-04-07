import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a1 = []
    a2 = []
    for i in a:
        if i % 2 == 0:
            a1.append(i)
        else:
            a2.append(i)
    cnt = 0
    tot = a1 + a2
    for i in range(len(tot)):
        for j in range(i+1, len(tot)):
            if math.gcd(tot[i],tot[j] * 2) > 1:
                cnt += 1
    print(cnt)