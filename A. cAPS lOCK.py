s1 = input()
s = list(s1)
if s1 == s1.upper():
    print(s1.lower())
elif s[0] == s[0].upper() and ("".join(s[1:])) == ("".join(s[1:])).lower():
    print(s1)
elif s[0] == s[0].lower() and ("".join(s[1:])) == ("".join(s[1:])).upper():
    t1 = s[0].upper()
    t = ("".join(s[1:])).lower()
    print(t1 + t)
elif s1 == s1.lower():
    print(s1)
elif s[0] == s[0].lower() and ("".join(s[1:])) != ("".join(s[1:])).upper() and ("".join(s[1:])) != ("".join(s[1:]).lower()):
    print(s1)
elif s[0] == s[0].upper() and ("".join(s[1:])) != ("".join(s[1:]).upper()) and ("".join(s[1:])) != ("".join(s[1:]).lower()):
    print(s1)