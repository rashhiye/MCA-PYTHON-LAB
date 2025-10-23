x=int(input('enter first number: '))
y=int(input('enter second number: '))
z=int(input('enter third number: '))
if x > y & x>z:
	print(x,"is the largest")
elif y > x and y > z:
	print(y,"is the largest")	
else:
	print(z,"is the largest")