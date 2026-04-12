for _ in range(int(input())):
    n = int(input())
    if n <= 6:
        print(15)
    elif n == 8 or n == 7:
        print(20)
    elif n == 9 or n == 10:
        print(25)
    else:
        if n % 10 == 0:
            print((n//10) * 25)
        elif n % 8 == 0:
            print((n // 8) * 20)
        elif n % 6 == 0:
            print((n // 6) * 15)
        else:
            if n % 8 == 2:
                tot = n // 8
                print(((tot-1) * 20) + 25)
            elif n % 6 == 4:
                tot = n // 6
                print(((tot-1) * 15) + 25)
            elif n % 10 == 5:
                print(((n // 10) * 25) + 15)
            elif n % 10 == 9:
                print(((n // 10) * 25) + 25)
            elif n % 6 == 5:
                print(((n // 6) * 15) + 15)
            elif n % 8 == 5 or n % 8 == 6:
                print(((n // 8) * 20) + 15)
            elif n % 10 == 7 :
                print(((n // 10) * 25) + 20)
            elif n % 10 == 5:
                print(((n // 10) * 25) + 15)
            elif n % 8 == 7:
                print(((n // 8) * 20) + 20)
            elif n % 8 == 1:
                tot = n // 8
                print(((tot-1) * 20) + 25)
            elif n % 6 == 1:
                tot = n // 6
                print(((tot-1) * 15) + 20)
            elif n % 6 == 2:
                tot = n // 6
                print(((tot-1) * 15) + 20)
            elif n % 6 == 3 and n % 8 == 3:
                tot = n // 6
                print(((tot -1) * 15) + 25)