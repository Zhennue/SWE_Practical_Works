class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        if not self.head:
            return
        current = self.head
        seen = set([current.data])
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

    def merge_sorted(self, other_list):
        merged_list = LinkedList()
        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            if current1.data < current2.data:
                merged_list.append(current1.data)
                current1 = current1.next
            else:
                merged_list.append(current2.data)
                current2 = current2.next

        while current1:
            merged_list.append(current1.data)
            current1 = current1.next

        while current2:
            merged_list.append(current2.data)
            current2 = current2.next

        return merged_list

# Testing the new methods
ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)
print("Middle element:", ll1.find_middle())  # Output: 3

# Cycle test
print("Has cycle:", ll1.has_cycle())  # Output: False

# Remove duplicates
ll2 = LinkedList()
ll2.append(1)
ll2.append(3)
ll2.append(2)
ll2.append(3)
ll2.append(1)
ll2.display()  # Output before removing duplicates: 1 -> 3 -> 2 -> 3 -> 1
ll2.remove_duplicates()
ll2.display()  # Output after removing duplicates: 1 -> 3 -> 2

# Merging two sorted lists
ll3 = LinkedList()
ll3.append(1)
ll3.append(3)
ll3.append(5)

ll4 = LinkedList()
ll4.append(2)
ll4.append(4)
ll4.append(6)

merged_list = ll3.merge_sorted(ll4)
merged_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6