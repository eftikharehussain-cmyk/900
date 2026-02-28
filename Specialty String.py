for _ in range(int(input())):
    n = int(input())
    s = input()
    cnt1 = 1
    lst = list(s)
    if n % 2 != 0:
        print("NO")
    else:
        i = n
        while n > 0:
            for i in range(len(lst)-1):
                if lst[i] == lst[i+1]:
                    lst[i] = "*"
                    lst[i+1] = "*"
            cnt = lst.count("*")
            if cnt == 0 and len(lst) > 0:
                print("NO")
                break
            else:
                n -= cnt
                lst1=[]
                for i in lst:
                    if i != "*":
                        lst1.append(i)
                lst = lst1
    if len(lst) == 0:
        print("YES")