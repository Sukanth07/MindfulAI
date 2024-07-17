"""
Given two linked list insert nodes of second list into first list at alternate positions of first list. For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. So, for this question first make two lists list1 and list2. Then in output merge them.

Input: list1: 3->7->9 , list2: 8->12
Output: 3->8->7->12->9

Input: list1: 5->9, list2: 4->11->15
Output: 5->4->9->11->15
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodeEnd(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.displayLL()
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

            self.displayLL()

    def alternateLL(self,l1_head,l2_head):
        new_node = Node(l1_head.data)
        self.head = new_node
        temp = self.head
        while l1_head != None or l2_head != None:
            try:
                l1_head = l1_head.next
                new_node =  Node(l2_head.data)
                temp.next = new_node
                l2_head = l2_head.next
                temp = temp.next
                new_node = Node(l1_head.data)
                temp.next = new_node
                temp = temp.next
            except:
                pass
        self.displayLL()

    def displayLL(self):
        if self.head == None:
            print("Head node is not initialized")
        else:
            temp = self.head
            while temp!=None:
                if temp.next != None:
                    print(temp.data,end="->")
                else:
                    print(temp.data)
                temp = temp.next
                
list1 = LinkedList()
list1.insertNodeEnd(3)
list1.insertNodeEnd(7)
list1.insertNodeEnd(11)
print("---------------------------------------")
list2 = LinkedList()
list2.insertNodeEnd(8)
list2.insertNodeEnd(12)
print("---------------------------------------")
list3 = LinkedList()
list3.alternateLL(list1.head, list2.head)
