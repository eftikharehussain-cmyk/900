for _ in range(int(input())):
    n1, d = input().split()
    n = input()
    if len(n) == 1:
        tot = n+d
        _max = int(tot)
    _max = int(n + d)
    for i in range(len(n)):
        new = n[:i] + d + n[i:]
        if int(new) > int(_max):
            _max = new
            new = ""
        else:
            new = ""
    print(_max)

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n1, d = input().split()
    n = input().strip()

    for i in range(len(n)):
        if d > n[i]:
            print(n[:i] + d + n[i:])
            break
    else:
        print(n + d)