for _ in range(int(input())):
    a, b, c, x, y = map(int, input().split())
    if a < x and b < y:
        if (a + b + c) < (x + y):
            print("NO")
        else:
            print("YES")
    elif a < x and b >= y:
        if (a + c) < x:
            print("NO")
        else:
            print("YES")
    elif b < y and a >= x:
        if (b + c) < y:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")