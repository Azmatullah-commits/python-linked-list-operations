# Count Total Nodes in Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        return count


# Creating Linked List
mylist = LinkedList()
mylist.head = Node(10)
mylist.head.next = Node(20)
mylist.head.next.next = Node(30)
mylist.head.next.next.next = Node(40)

# Display Result
print("Number of nodes:", mylist.count_nodes())