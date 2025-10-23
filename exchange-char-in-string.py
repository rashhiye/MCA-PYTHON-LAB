a=input('enter a string')
words=list(a)
if len(words)>1:
    t=words[0]
    words[0]=words[-1]
    words[-1]=t
print(''.join(words))