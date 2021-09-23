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

   

