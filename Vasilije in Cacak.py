for _ in range(int(input())):
    n, k, x = map(int, input().split())
    if n < k:
        print("NO")
    elif n == k: 
        if n*(n+1)//2 == x: print("YES")
        else:print("NO")
    elif n > k and k*(k+1)//2 > x :print("NO")
    elif n > k and k*(k+1)//2 < x :
        t = n-k
        tot = (n*(n+1)//2) - t*(t+1)//2
        if tot >= x:print("YES")
        else:print("NO")
    elif n > k and k*(k+1)//2 == x :print("YES")
