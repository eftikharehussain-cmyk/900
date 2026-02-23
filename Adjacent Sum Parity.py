for _ in range(int(input())):
    n = int(input())
    a = [x for x in map(int, input().split())]
    t = a.count(1)
    if t % 2 == 0:
        print("YES")
    else:
        print("NO")