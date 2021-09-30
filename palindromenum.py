def isPalindrome(n):
    status = True
    num_list = [char for char in str(n)]
    print(num_list)
    # count = 5
    # print(num_list[-count])
    # print(num_list[count-1])
    if n < 0:
        return False

    i = 1
    while status != False and i <= len(num_list)//2:
        print("pos:",i,num_list[i-1])
        if num_list[-i] == num_list[i-1]:
            status = True
        else:
            status = False
        i += 1
    return status
    


print(isPalindrome(1234567654321))