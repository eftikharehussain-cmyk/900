for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    ones = a.count(1)
    zeros = a.count(0)
    
    print(ones * (2 ** zeros))
