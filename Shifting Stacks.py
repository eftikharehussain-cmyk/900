for _ in range(int(input())):
    n = int(input())
    a = [x for x in map(int, input().split())]
    cnt = 0
    for i in range(len(a)-1):
        tot = a[i] - i
        a[i] = i
        a[i+1] += tot
        if a[i] >= a[i+1]:
            print("NO")
            cnt += 1
            break

    if cnt == 0:
        print("YES")