
def tester():
    # a = [1,3,5,6,7]
    # print(a[-1])
    # for idx, each in enumerate(a):
    #     if idx == len(a)-1:
    #         print(idx, each)
    #         print(a[idx])
    # for e in range(len(a)):
    #     print(e)
    # print("`~~~~~~")
    # l = [4,3,12,86,13,6]
    # for i in range(2,len(l)):
    #     print(i)
    # ll = [1,2,3,4,4,5]
    # a=0
    # while a < len(ll):
    #     print(ll[a])
    #     a += 1

    
    

    # print(len(l1))
    # if l2[6] and l1[7]:
    #     print("there")
    # else:
    #     print("not there")

    # i = 0
    # while i < total_len:
    #     print(i, l2[i])
    #     if l1[i] and l2[i]:
    #         print("yes",i, l1[i], l2[i])
    #     else:
    #         if l1[i]:
    #             print("its l1")
    #         elif l2[i]:
    #             print("its l2")
    #     i += 1

    a = {}
    a[2] = 22
    a[1] = 11
    value = 112
    if value in a.values():
        print("yes")
    
    # i = 0
    # a = [0,1,2,3,4,5,6]
    # while a[i] < 100000:
    #     print(a[i])
    #     i += 1
    
    d = {2:1111}
    print(d[2])
    if 2 in d: print(d[2])

    p = [1,2,3,4,5]
    if 24 in p:
        print(True)
tester()

def mtable(n):
    for col in range(0,n+1):
        if col == 0:
            print('  ',end='')
        else:
            print(col, end=' ')
    for row in range(1,n+1):
        print('\n')
        print(row, end=' ')
        for col in range(1,n+1):
            print(row*col, end=' ')
        
mtable(4)