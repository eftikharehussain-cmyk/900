for _ in range(int(input())):
    dragon = [x for x in map(int, input().split())]
    sloth = [ x for x in map(int, input().split())]
    dragon_s = sum(dragon)
    sloth_s = sum(sloth)
    if dragon_s < sloth_s and sloth_s <= (len(sloth) * 100):
        print("SLOTH")
    else:
        print("DRAGON")
    if sloth_s < dragon_s and dragon_s <= (len(dragon) * 100):
        print("DRAGON")
    else:
        print("SLOTH")
    if sloth_s == dragon_s:
        cnt = 0
        for i in range(len(sloth)):
            if sloth[i] > dragon[i]:
                print("SLOTH")
                break
            elif sloth[i] < dragon[i]:
                print("DRAGON")
                break
            else:
                cnt += 1
        if cnt == len(sloth):
            print("TIE")