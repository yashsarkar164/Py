def fact(num):
    mul = 1
    for i in range(1,num+1):
        mul *= i
    return mul

a = int(input("Enter a number : "))
print(f"Factorial of {a} is {fact(a)}")