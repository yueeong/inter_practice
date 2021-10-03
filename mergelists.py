class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self,head):
        self.head = None

class Solution():
    def __init__(self):
        pass
    def mergelists(self, l1, l2):
        headplaceholder = Node('-1000')
        tail = headplaceholder

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next # move it forward to last most node

       
        if l1:
            print("in l1",l1.val)
            tail.next = l1
        else:
            print("in l2",l2.val)
            tail.next = l2
        return headplaceholder.next

def linkedlistmaker(arr):
    head = Node(0)
    tail = head
    for each in arr:
        tail.next = Node(each)
        tail = tail.next
    return head.next #throwaway first head node since it's fake placeholder to start

def printlistnode(node):
    while node != None:
        print(node.val, end=' ')
        node = node.next

def merger(l1,l2):
    x = 0
    y = 0
    ml = []
    while x < len(l1) and y < len(l2):
        if l1[x] < l2[y]:
            ml.append(l1[x])
            x += 1
        else:
            ml.append(l2[y])
            y += 1
        
    print(x, len(l1))
    print(y, len(l2))
    while x < len(l1):
        ml.append(l1[x])
        x += 1
    
    while y < len(l2):
        ml.append(l2[y])
        y += 1

    return ml


def main():
    arr1 = [2,4,6,8,10,15,16]
    arr2 = [1,3,5,9,11,13,17,19]
    # makes llinked list from list/arr of numbers
    ln1 = linkedlistmaker(arr1)
    ln2 = linkedlistmaker(arr2)

    soln = Solution()
    # pass in the head node of the linked list
    # printlistnode(soln.mergelists(ln1,ln2))

    print(merger(arr1,arr2))


if __name__ == "__main__":
    main()




