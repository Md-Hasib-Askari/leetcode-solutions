class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def helper(node):
            if not node:
                return "null,"
            return str(node.val) + "," + helper(node.left) + helper(node.right)
        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def helper(values):
            if values[0] == "null":
                values.pop(0)
                return None
            root = TreeNode(int(values[0]))
            values.pop(0)
            root.left = helper(values)
            root.right = helper(values)
            return root
        values = data.split(",")
        root = helper(values)
        return root
    
if __name__ == "__main__":
    codec = Codec()
    # Example tree:
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    serialized = codec.serialize(root)
    print(f"Serialized: {serialized}")

    deserialized_root = codec.deserialize(serialized)
    def print_tree(node):
        if not node:
            return "null"
        return f"{node.val}, {print_tree(node.left)}, {print_tree(node.right)}"
    print(f"Deserialized Tree: {print_tree(deserialized_root)}")