
def tester():
    a = [1,3,5,6,7]
    print(a[-1])
    for idx, each in enumerate(a):
        if idx == len(a)-1:
            print(idx, each)
            print(a[idx])
    for e in range(len(a)):
        print(e)
    print("`~~~~~~")
    l = [4,3,12,86,13,6]
    for i in range(2,len(l)):
        print(i)
tester()