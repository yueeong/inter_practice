

class Calculator:
    def __init__(self):
        pass
    def twosummer(self, num_list:list, target:int):
        print(num_list)
        for index,each in enumerate(num_list):
            curr_index = index
            for id,entry in enumerate(num_list):
                if id != curr_index:
                    if entry + each == target:
                        return curr_index, id


def main():
    list_of_nums = [2,7,11,15]
    target = 9
    calculator = Calculator()
    print(calculator.twosummer(num_list=list_of_nums, target=target))
    list_of_nums = [3,2,2,4]
    target = 7
    print(calculator.twosummer(num_list=list_of_nums, target=target))


if __name__ == "__main__":
    main()