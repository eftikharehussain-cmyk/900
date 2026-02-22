n = int(input())
weks = n // 7
holidays = weks * 2
tot = n % 7
_min = holidays + max(0, tot - 5)
_max = holidays + min(2, tot)
print(_min, _max)