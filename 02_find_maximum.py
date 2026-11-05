# Find Maximum Value in Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find_max(self):
        if self.head is None:
            return None

        max_value = self.head.data
        temp = self.head.next

        while temp is not None:
            if temp.data > max_value:
                max_value = temp.data

            temp = temp.next

        return max_value


# Creating Linked List
mylist = LinkedList()
mylist.head = Node(15)
mylist.head.next = Node(8)
mylist.head.next.next = Node(40)
mylist.head.next.next.next = Node(25)

# Display Result
print("Maximum value:", mylist.find_max())