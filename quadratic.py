import math
import cmath
a=float(input('enter a'))
b=float(input('enter b'))
c=float(input('enter c'))

desc=b*b-4*a*c
if desc>0:
    d=(-b+(math.sqrt(desc)))/2*a
    d1=(-b-(math.sqrt(desc)))/2*a
    print('ROOTS ARE DISTINCT')
    print('root1=',d)
    print('root2=',d1)
elif desc==0:
    d=(-b+(math.sqrt(desc)))/2*a
    d1=(-b-(math.sqrt(desc)))/2*a
    print('THE ROOTS ARE SAME')
    print('root1=',d)
    print('root2=',d1)
       
elif desc<0:
    d=(-b+(cmath.sqrt(desc)))/2*a
    d1=(-b-(cmath.sqrt(desc)))/2*a
    print('ROOTS ARE COMPLEX')
    print('root1=',d,'+i',d1)
    print('root2=',d,'-i',d1)
else:
    print('INVALID INPUT')