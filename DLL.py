"""
Python program that has a double linked list and counts the number of items in the list
"""


class Node(object):

    # This class creates a single node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    class DLL(object):
        def __init__(self):
            self.head = None
            self.tail = None
            self.count = 0

        def append_i(self, data):
            # Append an item
            new_item = Node(data, None, None)
            if self.head is None:
                self.head = new_item
                self.tail = self.head
            else:
                new_item.prev = self.tail
                self.tail.next = new_item
                self.tail = new_item

            self.count += 1

    doubleLL = DLL()
    doubleLL.append_i('Chris')
    doubleLL.append_i('John')
    doubleLL.append_i('Ian')
    doubleLL.append_i('James')
    doubleLL.append_i('Kevin')
    doubleLL.append_i('Jack')

    print("The Linked List has a total item count of: ", doubleLL.count)
