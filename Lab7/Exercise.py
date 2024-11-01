from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # 1. Find the maximum value in the BST
    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value

    # 2. Count the total number of nodes in the BST
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if not node:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    # 3. Level-order traversal (breadth-first search)
    def level_order_traversal(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # 4. Find the height of the BST
    def find_height(self):
        return self._find_height_recursive(self.root)

    def _find_height_recursive(self, node):
        if not node:
            return -1
        left_height = self._find_height_recursive(node.left)
        right_height = self._find_height_recursive(node.right)
        return 1 + max(left_height, right_height)

    # 5. Check if the tree is a valid BST
    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_value, max_value):
        if not node:
            return True
        if not (min_value < node.value < max_value):
            return False
        return (self._is_valid_bst_recursive(node.left, min_value, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_value))

# Testing the methods
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Test find_max
print("Maximum value:", bst.find_max())  # Expected: 8

# Test count_nodes
print("Total nodes:", bst.count_nodes())  # Expected: 7

# Test level_order_traversal
print("Level-order traversal:", bst.level_order_traversal())  # Expected: [5, 3, 7, 2, 4, 6, 8]

# Test find_height
print("Height of BST:", bst.find_height())  # Expected: 2

# Test is_valid_bst
print("Is valid BST:", bst.is_valid_bst())  # Expected: True