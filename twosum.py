

class Calculator:
    def __init__(self):
        pass
    def twosummer(self, num_list:list[int], target:int) -> list[int]:
        print(num_list)
        for index,each in enumerate(num_list):
            curr_index = index
            
            for id,entry in enumerate(num_list):
                if id != curr_index:
                    if entry + each == target:
                        return [curr_index, id]
    
    def twosum(self, num_list:list[int], target:int) -> list[int]:
        hash_map = {}
        for i,num in enumerate(num_list):
            if (target - num) in hash_map:
                return [hash_map[(target-num)],i]
            else:
                hash_map[num] = i




def main():
    list_of_nums = [2,6,7,15]
    target = 9
    calculator = Calculator()
    # print(calculator.twosummer(num_list=list_of_nums, target=target))
    print(calculator.twosum(num_list=list_of_nums, target=target))

    # list_of_nums = [3,3]
    # target = 6
    # print(calculator.twosummer(num_list=list_of_nums, target=target))


if __name__ == "__main__":
    main()