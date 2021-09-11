
class SearchAlgo():
    def __init__(self):
        pass

    def binarysearch(self, num_list:int, target:int) -> int:
        print(num_list)
        print("Length list: " + str(len(num_list)))
        print("Target to find: " + str(target))
        idx_lo , idx_hi = 0 , len(num_list) - 1
        print(idx_lo, idx_hi)
        while idx_lo <= idx_hi:
            idx_mid = (idx_lo + idx_hi) // 2
            print("midpoint:", str(idx_mid), "idx_lo:", str(idx_lo), "idx_hi:",str(idx_hi) )
            if num_list[idx_mid] == target:
                return idx_mid
            elif num_list[idx_mid] < target:
                idx_hi = idx_mid - 1
            elif num_list[idx_mid] > target:
                idx_lo = idx_mid + 1


def main():
    searcher = SearchAlgo()
    print("Position in list that has your number: " + 
    str(searcher.binarysearch([22,18,16,15,11,6,3,1], 11)))

if __name__ == "__main__":
    main()



