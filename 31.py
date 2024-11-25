a = int(input("Enter the range: "))
arr =[]
for i in range(1,a+1):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            arr.append(i)
print(arr)