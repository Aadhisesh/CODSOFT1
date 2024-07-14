import math
print ("SIMPLE CALCULATOR")
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if a>b:
        a-=b
        return a
    else:
        b-=a
        return b
def mul(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print("The quotient is :%s",q)
    print("The remainder is :%s",r)
def sqr(a):
    x=math.sqrt(a)
    return x
while(True):
    print("\nChoose the operation:")
    
    a=int(input(" \n1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.SQUARE ROOT\n6.EXIT\n"))
    if a==1:
        n1=int(input("Enter the first number:"))
        n2=int(input("Enter the second number:"))
        s=sum(n1,n2)
        print("The sum is :%s"%s)
    elif a==2:
        n1=int(input("Enter the first number:"))
        n2=int(input("Enter the second number:"))
        s=sub(n1,n2)
        print("The difference is :%s",s)
    elif a==3:
        n1=int(input("Enter the first number:"))
        n2=int(input("Enter the second number:"))
        s=mul(n1,n2)
        print("The multiplied is :%s",s)
    elif a==4:
        n1=int(input("Enter the first number:"))
        n2=int(input("Enter the second number:"))
        div(n1,n2)
    elif a==5:
        n1=int(input("Enter the  number :"))
        s=sqr(n1)
        print("The square is :%s",s)
    else:
        print("you choose to exit")
        break
