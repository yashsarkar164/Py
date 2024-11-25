num = list(map(int,input("Enter numbers : ").split()))
even = []
for i in range(0,len(num)):
    if num[i]%2==0:
        even.append(num[i])

squared_numbers = [n ** 2 for n in even]

total = sum(squared_numbers)

print(f"Output {total}")