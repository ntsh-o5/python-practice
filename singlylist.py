class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Index must be non-negative")
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if current is None:
            raise IndexError("Index out of bounds")
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        if self.head is None:
            raise IndexError("Delete from empty list")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current.next and count < index - 1:
            current = current.next
            count += 1
        if current.next is None:
            raise IndexError("Index out of bounds")
        current.next = current.next.next

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values))

# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_start(5)
    sll.insert_at_index(2, 15)
    sll.display()  # Expected: 5 -> 10 -> 15 -> 20
    print(sll.search(15))  # Expected: 2
    print(sll.search(100))  # Expected: -1
    sll.delete_at_index(1)
    sll.display()  # Expected: 5 -> 15 -> 20

