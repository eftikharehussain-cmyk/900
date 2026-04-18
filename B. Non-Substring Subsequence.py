for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        li, ri = map(int, input().split())
        t = s[ri-1]
        tot = s[ri:]
        t1 =s[li-1]
        tot1 = s[:li-1]
        if t not in tot and t1 not in tot1:
            print("NO")
        else:
            print("YES")