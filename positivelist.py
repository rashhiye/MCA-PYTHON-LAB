n=int(input("Enter the limit"))
#generate positive list of numbers from a given list of integers
def a():
    li=[]
    for i in range(n):
        x=int(input("enter element"))
        li.append(x)

    newList=[x for x in li if x>0]
    print(newList)
a()
