# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for everyLevel in level:
                if everyLevel.left:
                    queue.append(everyLevel.left)
                if everyLevel.right:
                    queue.append(everyLevel.right)
            
            level = queue
            
        return depth