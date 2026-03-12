for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    x = a.count(2)
    b = a.count(1)
    t = x // 2
    cnt = 0
    if x%2 != 0:
        print(-1)
    elif x == 0:
        print(1)
    elif x % 2 == 0 and x > 0:
        for i in range(len(a)):
            if a[i] == 2 and t > 0:
                cnt += 1
            if cnt == t:
                print(i+1)
                break