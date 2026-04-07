# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # time: O(n + m)
        # compare each node and move in both trees togther, if one reaches the end, keep going with the other tree
        # if both roots are null return None
        if not root1 and not root2: 
            return None

        # get the new root
        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        newRoot = TreeNode(val1 + val2)

        # recursively do the left and right subtrees
        newRoot.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        newRoot.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return newRoot

