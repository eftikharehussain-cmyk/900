import math
for _ in range(int(input())):
    a, b, k = map(int, input().split())
    g = math.gcd(a, b)
    tot, tot1 = a//g, b//g
    if tot <= k and tot1 <= k:
        print(1)
    else:
        print(2)
