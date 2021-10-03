def singleNumber(nums):

    # using dict data structure method
    d = {}
    for idx,each in enumerate(nums):
        if each in d:
            print(each, d[each],"exists")
            d.pop(each)
        else:
            d[each] = idx
    print(d)
    print(list(d.keys())[0])
    return list(d.keys())[0]
     
    # bitwise XOR using ^ method
    res = 0
    for i in nums:
        print("--", res,i)
        res = res^i
        print(res)
    print("~~~~",res)

# print(singleNumber([4,1,2,1,2,3,3]))

def containsdupe(nums):
    d = {}
    for id,each in enumerate(nums):
        if each in d:
            return True
        else:
            d[each] = id

    return False

print(containsdupe([1,1,1,3,3,4,3,2,4,2]))
print(containsdupe([1,2,3,4]))
