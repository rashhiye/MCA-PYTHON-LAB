a=float(input("enter a"))
b=float(input("enter b"))
c=int(input('choose an option \n 1.addition \n 2.substraction \n 3.multiplication \n 4.division \n'))
if c==1:
    print("sum = ",a+b)
elif c==2:
     print("result after substraction = ",a-b)
elif c==3:
    print("multiplication = ",a*b)
elif c==4:
    print("division = ",a/b)
else:
    print("INVALID CHOICE")