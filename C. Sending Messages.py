for _ in range(int(input())):
    n, f, a, b = map(int, input().split())
    t = list(map(int, input().split()))
    cnt = f
    for i in range(n):
        if i == 0:
            cnt -= min(a * t[i], b)
        else:
            s = t[i] - t[i-1]
            cnt -= min(a * s, b)
    if cnt > 0:
        print("YES")
    else:
        print("NO")
