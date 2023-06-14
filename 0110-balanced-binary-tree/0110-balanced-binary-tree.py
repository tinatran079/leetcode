# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):

        def dfs(root):
            # base case - if root is empty / leaf node
            if not root:
                # balanced subtree with height 0 
                return [True, 0]

            # recursive calls to left and right subtrees
            left, right = dfs(root.left), dfs(root.right)
            # check if left subtree, right subtree, and their height diff is ok.
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # return result - balanced and max height between l and r substrees
            return [balanced, 1 + max(left[1], right[1])]

        # call dfs func on root of binary tree and return balanced status(first element)
        return dfs(root)[0]