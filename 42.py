num = list(map(int,input("Enter numbers : ").split()))

nodupl = []

for n in num:
    if n not in nodupl:
        nodupl.append(n)
print(nodupl)