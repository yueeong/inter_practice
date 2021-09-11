import time

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

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



def main():

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
