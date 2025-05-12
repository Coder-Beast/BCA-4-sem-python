def is_fibo(n):
    if n < 0:
        return False
    elif n<=1:
        return True
    
    a,b = 0,1
    while b<n:
        a,b = b,a+b
    return b==n

num = int(input("Enter A Number:"))
if is_fibo(num):
    print(num , "is a Fibonnaci number")
else:
    print(num , "is NOT a Fibonnaci number")
    