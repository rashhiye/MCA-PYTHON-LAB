disc1={}
limit=int(input('enter the number of elements'))
for i in range (limit):
    key=int(input(f'enter the key: {i+1}'))
    value=input(f'enter the value : {key}')
    disc1[key]=value
print('dictionary ascending order(default order):',disc1)
disc2 = dict(sorted(disc1.items(), reverse=True))
print('Dictionary in descending order:', disc2)