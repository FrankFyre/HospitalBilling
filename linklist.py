class LinkNode:
    def __init__(self, value=None, data=None):
        self.value = value
        self.data = data
        self.next = None
        # Value stores movie Ids
        # Data stores the dvddata


class LinkedList:
    def __init__(self):
        self.head = LinkNode()

    def insert(self, value, data):
        new_node = LinkNode(value, data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    # Prints in a list. each node returns a tuple
    def display(self):
        elems = ''
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elems = elems + f"({current_node.value}, {current_node.data})"
            if current_node.next is not None:
                elems = elems + f" --> "
        print(elems)

    def get_linked_data(self):
        rec = []
        node2 = self.head
        while node2:
            rec.append(node2.data)
            node2 = node2.next
        return rec

    def delete(self, value):
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

