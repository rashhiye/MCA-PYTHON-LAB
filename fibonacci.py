
def febonacci(number):

    if number<=1:
        return 1
    else:
       return febonacci(number-1)+febonacci(number-2)
number=int(input('Enter a number'))
for i in range(number):
    print(febonacci(i),end=" ")
            

        