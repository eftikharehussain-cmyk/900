# in code baraye in ast ke yak kaghaz ra malom nist ofoqi ya amodi para karda ma mebenim ke aya in kagha yak moraba boda
for _ in range(int(input())):
    a,b=map(int,input().split())
    a1,b1=map(int,input().split())
    _max = max(a,b)
    _max1 = max(a1,b1)
    _min = min(a,b)
    _min1 = min(a1,b1)
    if _max == _max1:
        if _min+_min1 == _max:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")