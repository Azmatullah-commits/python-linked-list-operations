# Delete a Node by Given Value

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete_by_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return

            temp = temp.next

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Test 1: Delete Middle Node
mylist = LinkedList()
mylist.head = Node(10)
mylist.head.next = Node(20)
mylist.head.next.next = Node(30)

print("Test 1: Delete Middle Node")
print("Before:")
mylist.display()

mylist.delete_by_value(20)

print("After:")
mylist.display()


# Test 2: Value Not Found
mylist = LinkedList()
mylist.head = Node(10)
mylist.head.next = Node(20)
mylist.head.next.next = Node(30)

print("\nTest 2: Value Not Found")
print("Before:")
mylist.display()

mylist.delete_by_value(50)

print("After:")
mylist.display()


# Test 3: Delete Head Node
mylist = LinkedList()
mylist.head = Node(10)

print("\nTest 3: Delete Head Node")
print("Before:")
mylist.display()

mylist.delete_by_value(10)

print("After:")
mylist.display()