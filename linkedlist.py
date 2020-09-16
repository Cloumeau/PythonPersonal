class Node(object):
    # Singly linked node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DLL(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, data):
       #Appends an item to the linked list
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1

    def iterate(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val

    def print_fw(self):
        for node in self.iterate():
            print(node)

    def insert_start(self, data):
        if self.head is not None:
            new_node = Node(data, None, None)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.count += 1


items = dLL()
items.append_item('Tom')
items.append_item('Mark')
items.append_item('Kevin')
items.append_item('Rob')
items.append_item('Dan')
items.append_item('Paul')

print("First List:")
items.print_fw()
print("\n Item appended to front of list:")
items.insert_start("Liam")
items.print_fw()