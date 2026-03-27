import math
n = int(input())
lst = []
def isprime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True
for i in range(2, n+1):
    if isprime(i) == True:
        lst.append(i)
cnt = 0
cnt1 = 0
for j in range(1, n+1):
    for k in lst:
        if j % k == 0:
            cnt += 1
    if cnt == 2:
        cnt1 += 1
        cnt = 0
    else:
        cnt = 0
print(cnt1)