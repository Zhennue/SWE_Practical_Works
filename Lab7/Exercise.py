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

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        if not self.head:
            return
        seen = set()
        current = self.head
        seen.add(current.data)
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node(0)
        tail = dummy
        current1, current2 = list1.head, list2.head

        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        tail.next = current1 if current1 else current2
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

# Test cases
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# Find middle element
print("Middle element:", ll.find_middle())  # Expected: 3

# Detect cycle
print("Has cycle:", ll.has_cycle())  # Expected: False

# Remove duplicates
ll.append(3)
ll.append(2)
ll.remove_duplicates()
print("After removing duplicates:")
ll.display()  # Expected: 1 -> 2 -> 3 -> 4 -> 5

# Merge two sorted lists
ll2 = LinkedList()
for value in [2, 4, 6, 8]:
    ll2.append(value)

merged_ll = LinkedList.merge_sorted(ll, ll2)
print("Merged sorted list:")
merged_ll.display()  # Expected: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> 8