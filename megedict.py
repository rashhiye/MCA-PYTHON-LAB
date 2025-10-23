dict1={}
limit1=int(input('enter the limit'))
for i in range (limit1):
    key=int(input(f'enter the key values{i+1}'))
    value=input(f'enter the values :{key}')
    dict1[key]=value


dict2={}
limit2=int(input('enter the limit'))
for i in range (limit2):
    key=int(input(f'enter the key values{i+1}'))
    value=input(f'enter the values :{key}')
    dict2[key]=value
print(dict1)
print(dict2)
dict3=dict1|dict2
print(dict3)