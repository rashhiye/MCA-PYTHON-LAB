def gcd():
    a=int(input("enter the fiurst number"))
    b=int(input("enter the second number"))
    while b!=0:
        a,b=a,b%b
    return a

gcd()