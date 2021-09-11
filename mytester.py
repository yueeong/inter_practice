
def tester():
    a = [1,3,5,6,7]
    print(a[-1])
    for idx, each in enumerate(a):
        if idx == len(a)-1:
            print(idx, each)

tester()