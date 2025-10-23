import datetime

current = datetime.datetime.now().year

year=int(input("Enter the final year"))
def leap():    
    for i in range(current,year+1):
        if (i%4==0 and i%100!=0) or i%400==0:
            print(i)
leap()


