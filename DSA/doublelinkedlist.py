class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # start of the list

    def insert_at_first(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.next
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_n_position(self, val, position):
        new_node = Node(val)

        # Insert at the beginning
        if position == 0:
            self.insert_at_beginning(val)
            return

        current = self.head
        count = 0

        # Move to node before target position
        while current and count < position - 1:
            current = current.next
            count += 1

        # Position is out of bounds
        if current is None:
            print("Position out of bound")
            return

        # Insert new_node
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node


# Delete node at a given position
def delete_n_position(self, position):
    if self.head is None:
        print("List is empty")
        return

    current = self.head
    count = 0

    # Delete first node
    if position == 0:
        self.head = current.next
        if self.head:
            self.head.prev = None
        return

    # Move to node to delete
    while current and count < position:
        current = current.next
        count += 1

    if current is None:
        print("Position out of bound")
        return

    # Remove node
    if current.next:
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next


# Traverse forward
def traverse_forward(self):
    current = self.head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


# Traverse backward
def traverse_backward(self):
    current = self.head
    if not current:
        return
    # Move to last node
    while current.next:
        current = current.next
    # Traverse backward
    while current:
        print(current.data, end=" ")
        current = current.prev
    print()
