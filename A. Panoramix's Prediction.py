a, b = map(int, input().split())
lst = []
for num in range(2,51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            lst.append(num)
if b not in lst:
    print("NO")
else:
    for i in range(len(lst)-1):
        if lst[i] == a:
            if lst[i+1] == b:
                print("YES")
            else:
                print("NO")
