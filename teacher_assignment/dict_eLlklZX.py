list1 =['a','a','a','b','b','c','c','d','d','d','d']
list2= list(set(list1))
def dictionary(list1, list2):
    thisdict=dict()
    for i in list2:
        count=0
        for j in list1:
            if i==j:
             count+=1
        print(count)
        print(i)
        
        thisdict[i]=count
    return thisdict
    
dicto=dictionary(list1, list2)
print(dicto)


