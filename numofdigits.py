a=int(input("enter an integer"))
count=0
while(a>0):
    r=a%10
    count=count+1
    a=a//10

print(count)