def sum_of_left_leaves(root):
    if not root:
        return 0
    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val
    return total + sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)
