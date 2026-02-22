# in kode baray tafawot max wa min dar yak antarwal moshakhas minimum on ra paida mekonad
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
i = 0
j = n - 1
lst1 = []
while j < m:
    tot = lst[j] - lst[i]
    lst1.append(tot)
    j += 1
    i += 1
print(min(lst1))
