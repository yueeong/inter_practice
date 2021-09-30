
# sort random arranged list
from mergelists import merger


def sortlist(l):
    for x in range(len(l)):
        for y in range(x+1,len(l)):
            if l[y] < l[x]:
                dummy = l[x]
                l[x] = l[y]
                l[y] = dummy
    print(l)
    

# sortlist([5,3,6,1,234,421,1,3,2,4,345,3,134])

def merger(l1,l2):
    print("merging", l1,l2)
    ml =[]
    x = 0
    y = 0

    while x < len(l1) and y < len(l2):
        if l1[x] < l2[y]:
            ml.append(l1[x])
            x += 1
        else:
            ml.append(l2[y])
            y += 1
    # print(x,y)
    if x == len(l1): ml.extend(l2[y:])
    else: ml.extend(l1[x:])   
    return ml 


def merge_sort(l):
    if len(l) <= 1:
        return l
    
    left_list, right_list = merge_sort(l[0:len(l)//2]) , merge_sort(l[len(l)//2:])
    

    merged_list = merger(left_list, right_list)
    return merged_list

print(merge_sort([5,3,6,1,234,421,44,5,7]))
f = [5,3,6,1,234,421,44,5,7]
# f.sort()
print(f)
print(sorted(f))