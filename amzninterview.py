# function input : 2 ordered lists 
# return single ordered list
# 1, 3, 6, 9, 10
# 0, 5, 12, 15, 17, 22

# 0, 1, 

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class InterviewFuncs():
    def __init__(self, sortedlist1:int, sortedlist2:int):
        self.sortedlist1 = sortedlist1
        self.sortedlist2 = sortedlist2

        self.l1 = self.converttolinkedlist(self.sortedlist1)
        self.l2 = self.converttolinkedlist(self.sortedlist2)

    def converttolinkedlist(self,arr):
        headplaceholder = Node(0)
        tail = headplaceholder

        for each in arr:
            tail.next = Node(each)
            tail = tail.next
        return headplaceholder.next

    def combineandsort(self):
        headplaceholder = Node(0)
        tail = headplaceholder

        while self.l1 and self.l2:
            if self.l1.val < self.l2.val:
                tail.next = self.l1
                self.l1 = self.l1.next
            else:
                tail.next = self.l2
                self.l2 = self.l2.next
            tail = tail.next
        
        if self.l1:
            tail.next = self.l1
        else:
            tail.next = self.l2

        return headplaceholder.next

def printlistnode(node):
    while node != None:
        print(node.val, end=' ')
        node = node.next

def main():

    thing = InterviewFuncs([1, 3, 6, 9, 10,13,16,21,22,33], [0, 5, 12, 15, 17,18,22, 22,24,26,27,28] )
    printlistnode(thing.combineandsort())
    

if __name__ == "__main__":
    main()

    # def binarysearch(self, num_list:int, target:int) -> int:
    #     idx_lo , idx_hi = 0 , len(num_list) - 1
    #     while idx_lo <= idx_hi:
    #         idx_mid = (idx_lo + idx_hi) // 2
    #         if num_list[idx_mid] == target:
    #             return idx_mid
    #         elif num_list[idx_mid] > target:
    #             idx_hi = idx_mid - 1
    #         elif num_list[idx_mid] < target:
    #             idx_lo = idx_mid + 1
        
    # def combineandsort(self):
                
    #     list1 = self.sortedlist1
    #     list2 = self.sortedlist2
    #     print("list1:", list1)
    #     print("list2:", list2)
    
    #     finalist = [-1]
        
    #     for idx,item in enumerate(list1):
            
    #         for index,each in enumerate(list2):
    #             # print(finalist)
    #             # print("Testing :", each , "vs" , item)
    #             if (each < item) :
    #                 print("list2 win")
    #                 print(finalist[-1])
    #                 if each > finalist[-1] :
    #                     finalist.append(each)
                            
    #             elif (item < each) :
    #                 print("list1 win")
    #                 print(finalist[-1])
    #                 if item > finalist[-1]:
    #                     finalist.append(item)
    #             print("index:", index)
    #         print("idx:", idx)

    #     finalist.pop(0)
    #     print("Combined list before check missing:", finalist)
    #     # check if all items used, use bin search to find items not inserted
    #     print("~~~~")
    #     extra = []
       

    #     for i in list1:
    #         if self.binarysearch(finalist,i) == None:
    #             extra.append(i)
        
    #     for j in list2:
    #         if self.binarysearch(finalist,j) == None:
    #             extra.append(j)
    #     print("Items skipped:", extra)

    #     total_list = finalist + extra

    #     print(total_list)



def main():

    thing = InterviewFuncs([1, 3, 6, 9, 10,13,16,21,33], [0, 5, 12, 15, 17,18, 22,24,26,27,28] )
    thing.combineandsort()

if __name__ == "__main__":
    main()