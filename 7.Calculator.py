def addition(x,y):
    return x + y
def substraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

def printing(op, n1,n2,val):
    print(f"the {op} of {n1} and {n2} is {val}")

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
c = int(input("Selection:"))

if(c == 1):
    printing("addition",num1,num2,addition(num1,num2))
elif c == 2:
    printing("substraction",num1,num2,substraction(num1,num2))
elif c == 3:
    printing("multiplication",num1,num2,multiply(num1,num2))
elif c == 4:
    if num2 ==0:
        print("Enter a positive value for num2")
    else:
        printing("division", num1,num2,division(num1,num2))
else:
    print("Invalid Input")
    