a, b, c, d = map(int, input().split())
misha = max(((3*a)// 10),a - (a// 250) * c)
wasia = max(((3 * b) // 10), b - (b // 250) * d)
if misha > wasia:
    print("Misha")
elif wasia > misha:
    print("Vasya")
else:
    print("Tie")