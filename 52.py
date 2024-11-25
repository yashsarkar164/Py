a = input("Enter a string : ")
vowel = ["A","E","I","O","U","a","e","i","o","u"]
count = 0

for i in range(0,len(a)):
    if a[i] in vowel:
        count+=1
cons = len(a)-count

print(f"Total vowel : {count}")
print(f"Total consonents : {cons}")