import math
for _ in range(int(input())):
    a, k = map(int, input().split())
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)+1)):
            if a % i == 0:
                return False
        return True
    cnt = 0
    if is_prime(a):
        cnt = a + a
        cnt += ((k-1) * 2)
    elif a % 2 != 0:
        cnt = a
        for j in range(2,a):
            if a % j == 0:
                cnt += j
                break
        cnt += ((k-1) * 2)
    else:
        cnt = a
        cnt += (k * 2)
    print(cnt)
