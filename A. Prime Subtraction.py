for _ in range(int(input())):
    x, y = map(int, input().split())
    tot = x - y
    if tot > 1:
        print("YES")
    else:
        print("NO")