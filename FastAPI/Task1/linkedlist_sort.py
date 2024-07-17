class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def swap(self, node1, node2):
        tmp = node1.data
        node1.data = node2.data
        node2.data = tmp

    def bubbleSort(self, head, ascending=True):
        if head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            curr = head
            while curr.next:
                if (curr.data > curr.next.data and ascending) or (curr.data < curr.next.data and not ascending):
                    self.swap(curr, curr.next)
                    swapped = True
                curr = curr.next
    
    def displayLinkedList(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements
    