for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    cnt = 0
    for i in range(len(a)-1):
        if a[i] % 2 == 0 and a[i+1] % 2 == 0 or a[i] % 2 != 0 and a[i+1] % 2 != 0:
            cnt += 1
    print(cnt)