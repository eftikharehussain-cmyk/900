n, x = map(int, input().split())
cnt = 0
for _ in range(n):
    ai, bi = input().split()
    if ai == "+":
        x += int(bi)
    else:
        if int(bi) > x:
            cnt += 1
        else:
            x-= int(bi)
print(x,cnt)