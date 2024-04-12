# Linkedlist practice

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.nextNode = self.head
            self.head = new_node

    def insertAtTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.insertAtHead(new_node)
        else:
            current = self.head
            while current.nextNode is not None:
                current = current.nextNode
            current.nextNode = new_node

    def insertAtPosition(self, data, position):
        new_node = Node(data)
        if self.head is None:
            self.insertAtHead(new_node)
        else:
            current_node = self.head
            pos = 0
            while current_node is not None and pos + 1 != position:
                current_node = current_node.nextNode
                pos += 1

            if current_node is not None:
                new_node.nextNode = current_node.nextNode
                current_node.nextNode = new_node
            else:
                print("Node does not exist")

    def __str__(self):
        current = self.head
        while current.nextNode is not None:
            print(current, '-> ', end='')
            current = current.nextNode


linked_list = LinkedList()
linked_list.insertAtHead("A")
linked_list.insertAtTail("B")
linked_list.insertAtTail("D")
linked_list.insertAtPosition("C", 3)

print(linked_list)
