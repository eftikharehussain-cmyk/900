n = int(input())
s = input()
i = 0
cnt = 0
while i < n:
    if s[i] == "1":
        cnt += 1
        i += 1
    else:
        if cnt == 0:
            i += 1
        else:
            break

if s[0] == "1" and cnt != n:
    print(cnt+1)
elif cnt+1 == n:
    print(1)
elif len(s) == 1 and s[0] == "0":
    print(1)
elif cnt == 0:
    print(1)
else:
    print(cnt)