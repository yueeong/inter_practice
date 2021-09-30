import time
from typing import Optional

class Node():
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    
    def printlist(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
        

class TreeNode():
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
    
def printInOrderTraverse(node:TreeNode):
    if node:
        printInOrderTraverse(node.left)
        print(node.value)
        printInOrderTraverse(node.right)

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def linkedlistmaker(arr):
    head = ListNode()
    tail = head
    for each in arr:
        tail.next = Node(each)
        tail = tail.next
    return head.next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    head = head
    tail = head
    tracking_list = []
    result_head = ListNode()
    result_tail = result_head
    while tail:
        if tail.value in tracking_list:
            tail = tail.next
        else:
            tracking_list.append(tail.value)
            print(tracking_list)
            result_tail.next = ListNode(tail.value)
            result_tail = result_tail.next
            tail = tail.next
            
    return result_head.next

def deldupes(head):
    tail = head
    while tail.next:
        if tail.value != tail.next.value:
            tail = tail.next
        else:
            tail.next = tail.next.next
    return head

def printlistnode(node):
    while node != None:
        print(node.value, end=' ')
        node = node.next

def main():
    dupelist = [1,1,2,3,4,5,5,5]
    ar = linkedlistmaker(dupelist)
    printlistnode(deleteDuplicates(ar))
    printlistnode(deldupes(ar))

    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.left.right.right = TreeNode(6)

    # printInOrderTraverse(root)

    # mylist = LinkedList()

    # mylist.head = Node(1)
    # Node(1).next = Node(2)
    # Node(2).next = Node(3)

    # mylist.printlist()



if __name__ == "__main__":
    main()
