for _ in range(int(input())):
    n = int(input())
    a = [x for x in map(int, input().split())]
    a.sort(reverse=True)
    alice = 0
    bob = 0
    for i in range(len(a)):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    if alice > bob:
        print("YES")
    else:
        print("NO")