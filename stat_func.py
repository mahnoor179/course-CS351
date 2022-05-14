#defining a function that returns mean
def mean(list1):
    sum = 0
    for i in list1:
        sum = sum +i
    avg= sum/len(list1)
    return avg
#defining a function that returns median
def median(list1):
    s = len(list1)
    list1.sort()
    if s%2 == 0:
        ind = int(s/2)
        med = (list1[ind-1]+list1[ind]/2)
    else:
        ind = s//2
        med = list1[ind]
    return med
#defining a function that returns mode
def mode(list1):
    count_list=[]
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    for i in list2:
        if i in list1:
            count_list.append(list1.count(i))
    max_count= max(count_list)
    if max_count ==1:
        return None
    else:
        ind = count_list.index(max_count)
        return list2[ind]
