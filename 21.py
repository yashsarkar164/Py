a = int(input("Enter a number : "))
count = 0
for i in range(1,a+1):
    if(a%i==0):
        count+=1
    else:
        continue
if(count>2):
    print("Not Prime")
else:
    print("Prime")
