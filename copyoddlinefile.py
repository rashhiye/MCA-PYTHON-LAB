#copy oddlines of one file to another
newfile = open("copy.txt","w")

file1=open("file1.txt","r")
file2=open("file2.txt","a")

count=0
for line in file1:
    count+=1
    if count%2!=0:
        file2.write(line)
