class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    # O(log(n)) | space: O(1)
    def insert(self, value):
        current_node = self

        while True:
            if value < current_node.value:
                # insert in the left tree

                if current_node.left:
                    current_node = current_node.left

                else:
                    # current_node has not left child
                    current_node.left = BST(value)
                    break

            else:
                if current_node.right:
                    current_node = current_node.right

                else:
                    # current_node has not right child
                    current_node.right = BST(value)
                    break

        return self

    # O(log(n)) | space: O(1)
    def search_value(self, value):
        current_node = self

        while current_node:
            if value < current_node.value:
                current_node = current_node.left

            elif value > current_node.value:
                current_node = current_node.right

            else:
                return True

        return False

    def remove(self, value, parent_node=None):
        current_node = self

        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left

            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right

            else:
                # found the node to be removed
                if current_node.left and current_node.right:
                    current_node.value = current_node.right.get_min_value()

                    # current node = smallest value of right subtree
                    current_node.right.remove(current_node.value, current_node)

                elif not parent_node:  # is the root node
                    if current_node.left:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left

                    elif current_node.right:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right

                    else:  # only root node exists in BST
                        current_node.value = None

                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left else current_node.right

                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left else current_node.right
