def occ():
    li=(input("Enter a line of words"))
    x=li.split()
    dic={}
    for item in x:
        dic[item]=0
    for item in dic:
        i=0
        for item2 in x:
            if item==item2:
                i=i+1
        dic[item]=i
    print("The number of occurance ")
    for item in dic:
        print("Item : %s,appreared %d time"%(item,dic[item]))
occ()
