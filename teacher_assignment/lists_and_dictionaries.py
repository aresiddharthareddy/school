list1 = ['a','a','a','b','b','c','c','d','d','d','d']
list2 = []
def lists(list1, list2):
    for i in list1:
        if i in list2:
            continue
        else:
            list2.append(i)
    print(list1)
    print(list2)
lists(list1, list2)