# remove duplicate of a set
list=[]
for i in range (0,8):
    list.append(i)
    list.append(6)
    list.append(8)
    print("created list which contain duplicate elements:",list)
    x=set(list)
    print("after creating set removes duplicate elements:",x)
    
