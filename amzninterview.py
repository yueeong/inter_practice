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

    def cands(self):
        mergedlist = []
        x = 0
        y = 0
        while x < len(self.sortedlist1) and y < len(self.sortedlist2):
            print(x,y)
            if self.sortedlist1[x] < self.sortedlist2[y]:
                mergedlist.append(self.sortedlist1[x])
                x += 1
            else:
                mergedlist.append(self.sortedlist2[y])
                y += 1
        
        print("stopped at counts:", x, y)
        while x < len(self.sortedlist1):
            mergedlist.append(self.sortedlist1[x])
            x += 1
        
        while y < len(self.sortedlist2):
            mergedlist.append(self.sortedlist2)
            y += 1
        print(mergedlist)


def printlistnode(node):
    while node != None:
        print(node.val, end=' ')
        node = node.next

def main():

    thing = InterviewFuncs([1, 5, 6,9,11], [2,4,6,10] )
    # printlistnode(thing.combineandsort())
    thing.cands()
    

if __name__ == "__main__":
    main()

   

