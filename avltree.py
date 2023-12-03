class AVLNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AvlBst(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, value):
        if not root:
            return AVLNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        elif value >= root.value:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        if balance < -1 and value >= root.right.value:
            return self.left_rotate(root)

        if balance > 1 and value >= root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, first_node):

        L_node = first_node.right
        child_node = L_node.left


        L_node.left = first_node
        first_node.right = child_node

        # Update the heights
        first_node.height = 1 + max(self.get_height(first_node.left),
                                    self.get_height(first_node.right))
        L_node.height = 1 + max(self.get_height(L_node.left),
                                self.get_height(L_node.right))

        # Return the new root
        return L_node

    def right_rotate(self, first_node):

        L_node = first_node.left
        child_node = L_node.right

        # Perform rotation
        L_node.right = first_node
        first_node.left = child_node

        # Update the  heights
        first_node.height = 1 + max(self.get_height(first_node.left),
                                    self.get_height(first_node.right))
        L_node.height = 1 + max(self.get_height(L_node.left),
                                self.get_height(L_node.right))

        # Return the new root
        return L_node

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def inorder(self, root):
        lister = []
        if root:
            lister = lister + self.inorder(root.left)
            lister.append(root.value)
            lister = lister + self.inorder(root.right)

        return lister

    def search(self, root, val):
        if not root or root.value == val:
            return root.value

        if root.value < val:
            return self.search(root.right, val)

        return self.search(root.left, val)

    def delete(self, root, key):
        if not root:
            return root

        elif key < root.value:
            root.left = self.delete(root.left, key)

        elif key > root.value:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root

        return self.get_min_value_node(root.left)

