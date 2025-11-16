class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # -----------------------------
    # INSERT
    # -----------------------------
    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)
        return self

    def _insert_recursive(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)

        return node

    # -----------------------------
    # SEARCH
    # -----------------------------
    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None:
            return None

        if data < node.data:
            return self._search_recursive(node.left, data)
        elif data > node.data:
            return self._search_recursive(node.right, data)
        else:
            return node

    # -----------------------------
    # FIND MIN / MAX
    # -----------------------------
    def find_min(self, node=None):
        node = node or self.root
        if node is None:
            return None

        while node.left:
            node = node.left
        return node

    def find_max(self, node=None):
        node = node or self.root
        if node is None:
            return None

        while node.right:
            node = node.right
        return node

    # -----------------------------
    # DELETE
    # -----------------------------
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)
        return self

    def _delete_recursive(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)

        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)

        else:
            # Case 1: no children
            if node.left is None and node.right is None:
                return None

            # Case 2: one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: two children
            max_left = self.find_max(node.left)
            node.data = max_left.data
            node.left = self._delete_recursive(node.left, max_left.data)

        return node

    # -----------------------------
    # VALIDATE BST
    # -----------------------------
    def is_bst(self):
        def validate(node, min_val, max_val):
            if node is None:
                return True
            if (min_val is not None and node.data <= min_val) or \
               (max_val is not None and node.data >= max_val):
                return False

            return validate(node.left, min_val, node.data) and \
                   validate(node.right, node.data, max_val)

        return validate(self.root, None, None)

    # -----------------------------
    # HEIGHT OF TREE
    # -----------------------------
    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return -1

        return max(self.height(node.left), self.height(node.right)) + 1

    # -----------------------------
    # CHECK IF BALANCED
    # -----------------------------
    def is_balanced(self):
        def check(node):
            if node is None:
                return 0

            left = check(node.left)
            if left == -1:
                return -1

            right = check(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return check(self.root) != -1

    # -----------------------------
    # BALANCE TREE
    # -----------------------------
    def balance(self):
        # inorder = sorted values
        arr = self.inorder()

        def build(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            node = Node(arr[mid])
            node.left = build(arr[:mid])
            node.right = build(arr[mid + 1:])
            return node

        self.root = build(arr)
        return self

    # -----------------------------
    # IN-ORDER TRAVERSAL
    # -----------------------------
    def inorder(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.data)
                traverse(node.right)

        traverse(self.root)
        return result

tree = BinarySearchTree()

tree.insert(5).insert(2).insert(8).insert(1).insert(3)

print(tree.search(3))          # Node found
print(tree.find_min().data)    # 1
print(tree.find_max().data)    # 8
print(tree.inorder())          # [1, 2, 3, 5, 8]

tree.delete(2)
print(tree.inorder())          # [1, 3, 5, 8]

print(tree.is_bst())           # True
print(tree.is_balanced())      # True / False depending on structure

tree.balance()
print(tree.is_balanced())      # True